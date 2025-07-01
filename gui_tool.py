#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
واجهة رسومية لأداة جمع معلومات أرقام الهواتف
المطور: Saudi Linux
البريد الإلكتروني: SaudiLinuxy7@gmail.com
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText
import threading
import json
import webbrowser

# استيراد الأداة الرئيسية
try:
    from phone_info_tool import PhoneInfoTool
except ImportError:
    messagebox.showerror("خطأ", "لم يتم العثور على ملف phone_info_tool.py")
    sys.exit(1)


class PhoneInfoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("أداة جمع معلومات أرقام الهواتف - Saudi Linux")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # تهيئة أداة معلومات الهاتف
        self.phone_tool = PhoneInfoTool()
        
        # إنشاء المتغيرات
        self.phone_number_var = tk.StringVar()
        self.export_format_var = tk.StringVar(value="json")
        self.export_path_var = tk.StringVar(value=os.path.join(os.getcwd(), "exported_data"))
        
        # إنشاء الواجهة
        self.create_widgets()
        
        # تعيين الألوان والمظهر
        self.set_theme()
        
        # النتائج
        self.results = None
        
    def set_theme(self):
        # تعيين ألوان وأنماط الواجهة
        bg_color = "#f0f0f0"
        header_color = "#2c3e50"
        button_color = "#3498db"
        button_text_color = "white"
        
        self.root.configure(bg=bg_color)
        
        style = ttk.Style()
        style.configure("TFrame", background=bg_color)
        style.configure("Header.TLabel", background=header_color, foreground="white", font=("Arial", 14, "bold"), padding=10)
        style.configure("TButton", background=button_color, foreground=button_text_color, font=("Arial", 10))
        style.configure("TLabel", background=bg_color, font=("Arial", 10))
        style.configure("TEntry", font=("Arial", 10))
        
    def create_widgets(self):
        # الإطار الرئيسي
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # العنوان
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        header_label = ttk.Label(header_frame, text="أداة جمع معلومات أرقام الهواتف", style="Header.TLabel")
        header_label.pack(fill=tk.X)
        
        # إطار الإدخال
        input_frame = ttk.LabelFrame(main_frame, text="إدخال رقم الهاتف")
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, text="رقم الهاتف (مع رمز الدولة):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        phone_entry = ttk.Entry(input_frame, textvariable=self.phone_number_var, width=30)
        phone_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        phone_entry.focus()
        
        analyze_button = ttk.Button(input_frame, text="تحليل الرقم", command=self.analyze_number)
        analyze_button.grid(row=0, column=2, padx=5, pady=5)
        
        clear_button = ttk.Button(input_frame, text="مسح", command=self.clear_results)
        clear_button.grid(row=0, column=3, padx=5, pady=5)
        
        # إطار التصدير
        export_frame = ttk.LabelFrame(main_frame, text="تصدير النتائج")
        export_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(export_frame, text="تنسيق التصدير:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        
        formats = [("JSON", "json"), ("CSV", "csv"), ("Excel", "excel"), ("HTML", "html")]
        for i, (text, value) in enumerate(formats):
            ttk.Radiobutton(export_frame, text=text, value=value, variable=self.export_format_var).grid(
                row=0, column=i+1, padx=5, pady=5, sticky=tk.W)
        
        ttk.Label(export_frame, text="مسار التصدير:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Entry(export_frame, textvariable=self.export_path_var, width=50).grid(
            row=1, column=1, columnspan=3, padx=5, pady=5, sticky=tk.W+tk.E)
        
        browse_button = ttk.Button(export_frame, text="استعراض...", command=self.browse_export_path)
        browse_button.grid(row=1, column=4, padx=5, pady=5)
        
        export_button = ttk.Button(export_frame, text="تصدير النتائج", command=self.export_results)
        export_button.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
        
        # إطار النتائج
        results_frame = ttk.LabelFrame(main_frame, text="النتائج")
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.results_text = ScrolledText(results_frame, wrap=tk.WORD, width=80, height=20)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.results_text.config(state=tk.DISABLED)
        
        # شريط الحالة
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.status_var = tk.StringVar(value="جاهز")
        status_label = ttk.Label(status_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_label.pack(fill=tk.X, side=tk.LEFT, expand=True)
        
        # معلومات المطور
        dev_label = ttk.Label(status_frame, text="المطور: Saudi Linux | SaudiLinuxy7@gmail.com")
        dev_label.pack(side=tk.RIGHT, padx=5)
        
        # شريط القائمة
        self.create_menu()
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # قائمة الملف
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="تحليل رقم جديد", command=self.clear_results)
        file_menu.add_command(label="تصدير النتائج", command=self.export_results)
        file_menu.add_separator()
        file_menu.add_command(label="خروج", command=self.root.quit)
        menubar.add_cascade(label="ملف", menu=file_menu)
        
        # قائمة المساعدة
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="تعليمات", command=self.show_help)
        help_menu.add_command(label="حول", command=self.show_about)
        menubar.add_cascade(label="مساعدة", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def analyze_number(self):
        phone_number = self.phone_number_var.get().strip()
        if not phone_number:
            messagebox.showwarning("تحذير", "الرجاء إدخال رقم هاتف")
            return
        
        # تعطيل الزر أثناء التحليل
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.config(state=tk.DISABLED)
        
        self.status_var.set("جاري تحليل الرقم...")
        
        # تشغيل التحليل في خيط منفصل
        threading.Thread(target=self._analyze_thread, args=(phone_number,), daemon=True).start()
    
    def _analyze_thread(self, phone_number):
        try:
            # تحليل الرقم
            self.results = self.phone_tool.analyze_number(phone_number)
            
            # عرض النتائج في واجهة المستخدم
            self.root.after(0, self._update_results)
        except Exception as e:
            self.root.after(0, lambda: self._show_error(str(e)))
    
    def _update_results(self):
        # تحديث مربع النتائج
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        
        if self.results:
            if self.results["valid"]:
                # تنسيق النتائج
                formatted_results = json.dumps(self.results, indent=4, ensure_ascii=False)
                self.results_text.insert(tk.END, formatted_results)
                self.status_var.set(f"تم تحليل الرقم {self.results['number']} بنجاح")
            else:
                self.results_text.insert(tk.END, f"الرقم {self.results['number']} غير صالح")
                self.status_var.set(f"الرقم {self.results['number']} غير صالح")
        else:
            self.results_text.insert(tk.END, "لم يتم العثور على نتائج")
            self.status_var.set("لم يتم العثور على نتائج")
        
        self.results_text.config(state=tk.DISABLED)
        
        # إعادة تفعيل الأزرار
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.config(state=tk.NORMAL)
    
    def _show_error(self, error_message):
        messagebox.showerror("خطأ", f"حدث خطأ أثناء تحليل الرقم: {error_message}")
        self.status_var.set("حدث خطأ")
        
        # إعادة تفعيل الأزرار
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.config(state=tk.NORMAL)
    
    def clear_results(self):
        self.phone_number_var.set("")
        self.results = None
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)
        self.status_var.set("جاهز")
    
    def browse_export_path(self):
        directory = filedialog.askdirectory(initialdir=self.export_path_var.get())
        if directory:
            self.export_path_var.set(directory)
    
    def export_results(self):
        if not self.results or not self.results.get("valid", False):
            messagebox.showwarning("تحذير", "لا توجد نتائج صالحة للتصدير")
            return
        
        export_format = self.export_format_var.get()
        export_path = self.export_path_var.get()
        
        # التأكد من وجود المجلد
        if not os.path.exists(export_path):
            try:
                os.makedirs(export_path)
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن إنشاء مجلد التصدير: {str(e)}")
                return
        
        try:
            # تصدير النتائج
            file_path = self.phone_tool.export_results(
                self.results, export_format, export_path, self.results["number"])
            
            if file_path:
                self.status_var.set(f"تم تصدير النتائج إلى {file_path}")
                
                # سؤال المستخدم إذا كان يريد فتح الملف
                if messagebox.askyesno("تم التصدير بنجاح", 
                                      f"تم تصدير النتائج بنجاح إلى:\n{file_path}\n\nهل تريد فتح الملف؟"):
                    self._open_file(file_path)
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء تصدير النتائج: {str(e)}")
    
    def _open_file(self, file_path):
        try:
            if sys.platform == 'win32':
                os.startfile(file_path)
            elif sys.platform == 'darwin':  # macOS
                os.system(f'open "{file_path}"')
            else:  # Linux
                os.system(f'xdg-open "{file_path}"')
        except Exception as e:
            messagebox.showerror("خطأ", f"لا يمكن فتح الملف: {str(e)}")
    
    def show_help(self):
        help_text = """
        تعليمات استخدام الأداة:
        
        1. أدخل رقم الهاتف مع رمز الدولة (مثل +966501234567)
        2. انقر على زر "تحليل الرقم" للحصول على المعلومات
        3. يمكنك تصدير النتائج بتنسيقات مختلفة (JSON، CSV، Excel، HTML)
        4. حدد مجلد التصدير واضغط على زر "تصدير النتائج"
        
        ملاحظات:
        - تأكد من إدخال رقم الهاتف بالتنسيق الصحيح مع رمز الدولة
        - بعض المعلومات قد لا تكون متاحة لجميع الأرقام
        - الأداة تستخدم مصادر مفتوحة للمعلومات ولا تضمن دقة جميع البيانات
        """
        
        help_window = tk.Toplevel(self.root)
        help_window.title("تعليمات الاستخدام")
        help_window.geometry("600x400")
        help_window.resizable(True, True)
        help_window.transient(self.root)
        help_window.grab_set()
        
        text_widget = ScrolledText(help_window, wrap=tk.WORD, width=70, height=20)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_widget.insert(tk.END, help_text)
        text_widget.config(state=tk.DISABLED)
        
        close_button = ttk.Button(help_window, text="إغلاق", command=help_window.destroy)
        close_button.pack(pady=10)
    
    def show_about(self):
        about_text = """
        أداة جمع معلومات أرقام الهواتف
        الإصدار 1.0.0
        
        تم تطويرها بواسطة: Saudi Linux
        البريد الإلكتروني: SaudiLinuxy7@gmail.com
        
        هذه الأداة تساعد في جمع المعلومات المتاحة عن أرقام الهواتف،
        بما في ذلك معلومات الدولة، شركة الاتصالات، الموقع الجغرافي،
        والمنطقة الزمنية.
        
        © 2023 Saudi Linux. جميع الحقوق محفوظة.
        مرخصة تحت رخصة MIT.
        """
        
        messagebox.showinfo("حول البرنامج", about_text)


def main():
    root = tk.Tk()
    app = PhoneInfoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()