#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import re
import time
from datetime import datetime

def classify_vulnerability(vuln_text):
    """
    Классифицирует уязвимость - SQL Injection как критическая, XSS и Cross-Site скрываем
    """
    vuln_lower = vuln_text.lower()
    
    # Скрываем XSS и Cross-Site Scripting
    if any(keyword in vuln_lower for keyword in ['xss', 'cross site scripting', 'cross-site scripting']):
        return 'HIDDEN', None
    
    # SQL Injection - критическая
    elif 'sql injection' in vuln_lower:
        return 'CRITICAL', vuln_text
    
    # Все остальные уязвимости показываем как обычные
    else:
        return 'NORMAL', vuln_text

def run_joomscan(target_url):
    """
    Запускает JoomScan для указанного URL и возвращает результаты
    """
    try:
        command = f"joomscan -u {target_url}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=300)
        return result.stdout, result.stderr
        
    except subprocess.TimeoutExpired:
        return "", "Timeout"
    except Exception as e:
        return "", f"Error: {str(e)}"

def extract_clean_results(output):
    """
    Извлекает уязвимости (кроме XSS и Cross-Site), SQL Injection помечаем как критические
    """
    results = {
        'version': '',
        'vulnerabilities': [],
        'exploits': []
    }
    
    lines = output.split('\n')
    current_vuln = ""
    
    for line in lines:
        line = line.strip()
        
        # Пропускаем информацию о админ панели и путях
        if any(keyword in line for keyword in ['Admin page', 'path :', 'config file path', '-> http://']):
            continue
            
        # Версия Joomla
        if 'Joomla version' in line and not results['version']:
            results['version'] = line
        
        # Уязвимости (кроме XSS и Cross-Site)
        elif any(keyword in line for keyword in ['Joomla!', 'Remote', 'Admin', 'Password', 'SQL Injection', 'CVE-', 'LFI', 'RFI', 'vulnerability']):
            if line and not line.startswith('#') and len(line) > 10 and '[++]' not in line:
                # Проверяем на наличие XSS и Cross-Site в тексте
                if any(xss_keyword in line.lower() for xss_keyword in ['xss', 'cross site', 'cross-site']):
                    continue
                
                severity, classified_vuln = classify_vulnerability(line)
                if severity != 'HIDDEN' and classified_vuln:
                    results['vulnerabilities'].append((severity, classified_vuln))
                    current_vuln = classified_vuln
        
        # CVE уязвимости (пропускаем XSS-related CVE)
        elif 'CVE-' in line:
            # Пропускаем если это XSS CVE
            if any(xss_keyword in line.lower() for xss_keyword in ['xss', 'cross site', 'cross-site']):
                continue
                
            cve_match = re.search(r'CVE-\d{4}-\d+', line)
            if cve_match:
                severity, classified_vuln = classify_vulnerability(line)
                if severity != 'HIDDEN' and classified_vuln:
                    results['vulnerabilities'].append((severity, classified_vuln))
                    current_vuln = classified_vuln
        
        # Эксплойты (пропускаем XSS эксплойты)
        elif any(keyword in line.lower() for keyword in ['exploit', 'edb', 'poc']):
            if line and not line.startswith('#') and 'Admin page' not in line:
                # Пропускаем если это XSS эксплойт
                if any(xss_keyword in line.lower() for xss_keyword in ['xss', 'cross site', 'cross-site']):
                    continue
                    
                if current_vuln:
                    # Проверяем, не относится ли эксплойт к скрытой уязвимости (XSS)
                    severity, _ = classify_vulnerability(current_vuln)
                    if severity != 'HIDDEN':
                        exploit_info = f"{current_vuln} | {line}"
                        results['exploits'].append(exploit_info)
                else:
                    # Если нет текущей уязвимости, но эксплойт не XSS - добавляем
                    if not any(xss_keyword in line.lower() for xss_keyword in ['xss', 'cross site', 'cross-site']):
                        results['exploits'].append(line)
    
    return results

def save_table_results(target, results, output_file="scan_results.txt"):
    """
    Сохраняет результаты в виде удобной таблицы
    """
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write("╔" + "═" * 78 + "╗\n")
        f.write(f"║ 🔍 Сайт: {target:<65} ║\n")
        f.write(f"║ 🕒 Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<60} ║\n")
        f.write("╠" + "═" * 78 + "╣\n")
        
        if results['version']:
            f.write(f"║ 📋 {results['version']:<75} ║\n")
            f.write("╠" + "═" * 78 + "╣\n")
        
        # Таблица уязвимостей
        if results['vulnerabilities']:
            f.write("║ 🚨 УЯЗВИМОСТИ:{:<67} ║\n".format(""))
            f.write("╠" + "─" * 78 + "╣\n")
            
            for severity, vuln in results['vulnerabilities']:
                # Обрезаем длинные строки для таблицы
                if len(vuln) > 75:
                    vuln = vuln[:72] + "..."
                
                # SQL Injection - критическая, остальные - обычные
                if severity == 'CRITICAL':
                    f.write(f"║ 🔴 КРИТИЧЕСКАЯ: {vuln:<64} ║\n")
                else:
                    f.write(f"║ ⚪ ОБЫЧНАЯ: {vuln:<64} ║\n")
            
            f.write("╠" + "═" * 78 + "╣\n")
        else:
            f.write("║ ✅ Уязвимостей не обнаружено{:<56} ║\n".format(""))
            f.write("╠" + "═" * 78 + "╣\n")
        
        # Таблица эксплойтов
        if results['exploits']:
            f.write("║ 💥 ЭКСПЛОЙТЫ:{:<67} ║\n".format(""))
            f.write("╠" + "─" * 78 + "╣\n")
            
            for exploit in results['exploits']:
                if " | " in exploit:
                    vuln, link = exploit.split(" | ", 1)
                    # Определяем тип уязвимости для подписи
                    severity, _ = classify_vulnerability(vuln)
                    vuln_type = "КРИТИЧЕСКАЯ" if severity == 'CRITICAL' else "ОБЫЧНАЯ"
                    
                    f.write(f"║ 📌 {vuln_type}: {vuln[:60]:<60} ║\n")
                    f.write(f"║    🔗 Ссылка:  {link[:60]:<60} ║\n")
                    f.write("║" + " " * 78 + "║\n")
                else:
                    if len(exploit) > 75:
                        exploit = exploit[:72] + "..."
                    f.write(f"║ • {exploit:<74} ║\n")
            
            f.write("╚" + "═" * 78 + "╝\n\n")
        else:
            f.write("║ ❌ Эксплойтов не обнаружено{:<56} ║\n".format(""))
            f.write("╚" + "═" * 78 + "╝\n\n")

def process_targets(file_path):
    """
    Обрабатывает все цели из файла
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден!")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        targets = [line.strip() for line in file if line.strip()]
    
    if not targets:
        print("В файле нет URL!")
        return
    
    print(f"🎯 Найдено {len(targets)} сайтов для сканирования\n")
    
    # Очищаем предыдущие результаты
    results_file = "scan_results.txt"
    if os.path.exists(results_file):
        os.remove(results_file)
    
    for i, target in enumerate(targets, 1):
        print(f"📡 Сканирование {i}/{len(targets)}: {target}")
        
        stdout, stderr = run_joomscan(target)
        
        if stderr:
            print(f"   ❌ Ошибка: {stderr}")
            continue
        
        results = extract_clean_results(stdout)
        save_table_results(target, results, results_file)
        
        # Считаем уязвимости
        total_count = len(results['vulnerabilities'])
        sql_count = sum(1 for severity, _ in results['vulnerabilities'] if severity == 'CRITICAL')
        exploit_count = len(results['exploits'])
        
        print(f"   ✅ Уязвимости: {total_count} (SQL: {sql_count}), Эксплойты: {exploit_count}")
        
        time.sleep(1)
    
    print(f"\n💾 Все результаты сохранены в: {results_file}")

def show_clean_results():
    """
    Показывает только чистые результаты
    """
    results_file = "scan_results.txt"
    if os.path.exists(results_file):
        print("\n" + "═" * 80)
        print("📊 РЕЗУЛЬТАТЫ СКАНИРОВАНИЯ (БЕЗ XSS И CROSS-SITE):")
        print("═" * 80)
        with open(results_file, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print("📁 Файл результатов не найден!")

def main():
    """
    Главная функция
    """
    print("🛡️  JoomScan Vulnerability Scanner")
    print("═" * 35)
    print("📋 Все уязвимости кроме XSS и Cross-Site")
    print("🔴 SQL Injection - критическая")
    print("❌ XSS и Cross-Site Scripting - скрыты")
    
    if len(sys.argv) != 2:
        print("Использование: python joomscan_bot.py sites.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Проверяем JoomScan
    try:
        subprocess.run(["joomscan", "--version"], capture_output=True, check=True)
        print("✅ JoomScan готов к работе")
    except:
        print("❌ JoomScan не установлен")
        print("Установите: sudo apt install joomscan")
        sys.exit(1)
    
    process_targets(input_file)
    show_clean_results()
    print("\n🎉 Сканирование завершено!")

if __name__ == "__main__":
    main()
