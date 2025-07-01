# توثيق واجهة برمجة التطبيقات (API) لأداة جمع معلومات أرقام الهواتف

هذا المستند يشرح كيفية استخدام أداة جمع معلومات أرقام الهواتف كمكتبة في مشاريعك الخاصة.

## الاستخدام الأساسي

```python
from phone_info_tool import PhoneInfoTool

# إنشاء كائن من الأداة
tool = PhoneInfoTool()

# تحليل رقم هاتف
phone_number = "+966501234567"
tool.analyze_number(phone_number)

# عرض النتائج
tool.display_results()

# تصدير النتائج
tool.export_results(format_type='json', filename='my_results')
```

## الفئات والدوال

### الفئة الرئيسية: `PhoneInfoTool`

#### الدالة: `__init__()`

تهيئة الأداة وعرض الشعار.

**المعاملات:** لا يوجد

**القيمة المرجعة:** كائن من نوع `PhoneInfoTool`

#### الدالة: `validate_phone_number(phone_number)`

التحقق من صحة تنسيق رقم الهاتف.

**المعاملات:**
- `phone_number` (سلسلة نصية): رقم الهاتف المراد التحقق منه

**القيمة المرجعة:**
- كائن `phonenumbers.PhoneNumber` إذا كان الرقم صحيحًا
- `None` إذا كان الرقم غير صحيح

#### الدالة: `get_basic_info()`

الحصول على المعلومات الأساسية عن رقم الهاتف.

**المعاملات:** لا يوجد (تستخدم `self.parsed_number`)

**القيمة المرجعة:**
- `True` إذا نجحت العملية
- `False` إذا فشلت العملية

#### الدالة: `get_geolocation()`

الحصول على معلومات الموقع الجغرافي لرقم الهاتف.

**المعاملات:** لا يوجد (تستخدم `self.parsed_number`)

**القيمة المرجعة:**
- `True` إذا نجحت العملية
- `False` إذا فشلت العملية

#### الدالة: `get_timezone_info()`

الحصول على معلومات المنطقة الزمنية لرقم الهاتف.

**المعاملات:** لا يوجد (تستخدم `self.parsed_number`)

**القيمة المرجعة:**
- `True` إذا نجحت العملية
- `False` إذا فشلت العملية

#### الدالة: `search_online_databases()`

البحث في قواعد البيانات عبر الإنترنت عن معلومات إضافية.

**المعاملات:** لا يوجد (تستخدم `self.parsed_number`)

**القيمة المرجعة:**
- `True` إذا نجحت العملية
- `False` إذا فشلت العملية

#### الدالة: `analyze_number(phone_number)`

تحليل رقم الهاتف المقدم وجمع جميع المعلومات المتاحة.

**المعاملات:**
- `phone_number` (سلسلة نصية): رقم الهاتف المراد تحليله

**القيمة المرجعة:**
- `True` إذا نجح التحليل
- `False` إذا فشل التحليل

#### الدالة: `display_results()`

عرض المعلومات التي تم جمعها بطريقة منسقة.

**المعاملات:** لا يوجد

**القيمة المرجعة:** لا يوجد

#### الدالة: `export_results(format_type='json', filename=None)`

تصدير النتائج إلى ملف بالتنسيق المحدد.

**المعاملات:**
- `format_type` (سلسلة نصية، اختياري): تنسيق التصدير ('json', 'csv', 'excel', 'html'). الافتراضي هو 'json'
- `filename` (سلسلة نصية، اختياري): اسم الملف المراد التصدير إليه. إذا لم يتم تحديده، سيتم إنشاء اسم ملف تلقائيًا

**القيمة المرجعة:**
- `True` إذا نجح التصدير
- `False` إذا فشل التصدير

## هيكل البيانات

تخزن النتائج في قاموس `self.results` بالهيكل التالي:

```python
{
    'basic_info': {
        'formatted_number': str,
        'country_code': int,
        'national_number': int,
        'country': str,
        'carrier': str,
        'time_zones': list,
        'is_valid': bool,
        'is_possible': bool,
        'number_type': str
    },
    'geolocation': {
        'country': str,
        'region': str,
        'coordinates': {
            'latitude': float or str,
            'longitude': float or str
        }
    },
    'timezone_info': [
        {
            'name': str,
            'current_time': str
        }
    ],
    'online_databases': {
        'spam_score': str,
        'reported_count': int,
        'last_reported': str,
        'tags': list,
        'note': str
    }
}
```

## أمثلة متقدمة

### استخدام الأداة في سكريبت

```python
from phone_info_tool import PhoneInfoTool

def process_phone_numbers(phone_numbers):
    results = []
    tool = PhoneInfoTool()
    
    for number in phone_numbers:
        if tool.analyze_number(number):
            # استخراج المعلومات المهمة فقط
            country = tool.results.get('basic_info', {}).get('country', 'Unknown')
            carrier = tool.results.get('basic_info', {}).get('carrier', 'Unknown')
            number_type = tool.results.get('basic_info', {}).get('number_type', 'Unknown')
            
            results.append({
                'number': number,
                'country': country,
                'carrier': carrier,
                'type': number_type
            })
    
    return results

# استخدام الدالة
phone_list = ["+1 555-123-4567", "+44 20 7946 0958", "+966 50 123 4567"]
results = process_phone_numbers(phone_list)
print(results)
```

### دمج الأداة مع واجهة مستخدم رسومية

```python
import tkinter as tk
from tkinter import messagebox, filedialog
from phone_info_tool import PhoneInfoTool

class PhoneInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("أداة معلومات الهاتف")
        self.tool = PhoneInfoTool()
        
        # إنشاء واجهة المستخدم
        self.create_widgets()
    
    def create_widgets(self):
        # إدخال رقم الهاتف
        tk.Label(self.root, text="أدخل رقم الهاتف:").grid(row=0, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(self.root, width=30)
        self.phone_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # زر التحليل
        tk.Button(self.root, text="تحليل الرقم", command=self.analyze).grid(row=1, column=0, columnspan=2, pady=10)
        
        # منطقة النتائج
        self.result_text = tk.Text(self.root, width=60, height=20)
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        # زر التصدير
        tk.Button(self.root, text="تصدير النتائج", command=self.export).grid(row=3, column=0, columnspan=2, pady=10)
    
    def analyze(self):
        phone_number = self.phone_entry.get()
        if not phone_number:
            messagebox.showerror("خطأ", "الرجاء إدخال رقم هاتف")
            return
        
        # مسح النتائج السابقة
        self.result_text.delete(1.0, tk.END)
        
        # تحليل الرقم
        if self.tool.analyze_number(phone_number):
            # عرض النتائج في مربع النص
            if 'basic_info' in self.tool.results:
                basic = self.tool.results['basic_info']
                self.result_text.insert(tk.END, f"الرقم: {basic['formatted_number']}\n")
                self.result_text.insert(tk.END, f"الدولة: {basic['country']}\n")
                self.result_text.insert(tk.END, f"شركة الاتصالات: {basic['carrier']}\n")
                self.result_text.insert(tk.END, f"نوع الرقم: {basic['number_type']}\n\n")
            
            if 'geolocation' in self.tool.results:
                geo = self.tool.results['geolocation']
                self.result_text.insert(tk.END, f"المنطقة: {geo['region']}\n")
                self.result_text.insert(tk.END, f"الإحداثيات: {geo['coordinates']['latitude']}, {geo['coordinates']['longitude']}\n\n")
            
            if 'timezone_info' in self.tool.results:
                for tz in self.tool.results['timezone_info']:
                    self.result_text.insert(tk.END, f"المنطقة الزمنية: {tz['name']}\n")
                    self.result_text.insert(tk.END, f"الوقت الحالي: {tz['current_time']}\n\n")
        else:
            self.result_text.insert(tk.END, "فشل في تحليل رقم الهاتف. تأكد من إدخال رقم صحيح.")
    
    def export(self):
        if not hasattr(self.tool, 'results') or not self.tool.results:
            messagebox.showerror("خطأ", "لا توجد نتائج للتصدير. قم بتحليل رقم هاتف أولاً.")
            return
        
        # اختيار مكان حفظ الملف
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv"), 
                       ("Excel files", "*.xlsx"), ("HTML files", "*.html")]
        )
        
        if file_path:
            # تحديد نوع التصدير من امتداد الملف
            ext = file_path.split(".")[-1]
            format_map = {"json": "json", "csv": "csv", "xlsx": "excel", "html": "html"}
            format_type = format_map.get(ext, "json")
            
            # تصدير النتائج
            if self.tool.export_results(format_type, file_path.rsplit(".", 1)[0]):
                messagebox.showinfo("نجاح", f"تم تصدير النتائج بنجاح إلى {file_path}")
            else:
                messagebox.showerror("خطأ", "فشل في تصدير النتائج")

# تشغيل التطبيق
if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneInfoApp(root)
    root.mainloop()
```

## ملاحظات للمطورين

1. يمكن توسيع الأداة بسهولة عن طريق إضافة طرق جديدة لجمع المعلومات.
2. للاتصال بقواعد بيانات حقيقية، يمكنك تعديل الدالة `search_online_databases()` لاستخدام واجهات برمجة تطبيقات حقيقية.
3. يمكن تحسين أداء الأداة عن طريق تخزين النتائج مؤقتًا لتجنب تكرار الاستعلامات.
4. للاستخدام في بيئة إنتاجية، يُنصح بإضافة المزيد من التعامل مع الأخطاء والتسجيل.

## المساهمة

إذا كنت ترغب في المساهمة في تطوير هذه الأداة، يرجى اتباع الخطوات التالية:

1. انسخ المستودع (Fork)
2. أنشئ فرعًا جديدًا للميزة التي ترغب في إضافتها
3. قم بإجراء التغييرات اللازمة
4. أرسل طلب سحب (Pull Request)

## الاتصال

إذا كان لديك أي أسئلة أو اقتراحات، يرجى التواصل مع المطور:

- البريد الإلكتروني: SaudiLinuxy7@gmail.com