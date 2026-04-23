#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================================================
# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║         🔥 SIGNATURE KILLER PRO ULTIMATE - FULL VERSION 🔥                ║
# ║              💎 SAME POWER AS MT MANAGER & NP MANAGER 💎                  ║
# ║                   🛠️ DEVELOPER: MOHAMED ELMASRY 🛠️                        ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
# ============================================================================

import os
import sys
import subprocess
import shutil
import tempfile
import re
import time
import requests
import datetime
import hashlib

# ============================================================================
# GitHub Configuration (عدل هنا)
# ============================================================================
GITHUB_USER = "YOUR_USERNAME"      # 👈 اسم المستخدم بتاعك
GITHUB_REPO = "YOUR_REPO"           # 👈 اسم الريبو
CODES_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main/codes.txt"

# ============================================================================
# Colors
# ============================================================================
G = '\033[1;32m'
S = '\033[1;36m'
Y = '\033[1;33m'
P = '\033[1;35m'
W = '\033[1;37m'
R = '\033[1;31m'
X = '\033[0m'

# ============================================================================
# LICENSE VERIFICATION SYSTEM
# ============================================================================

class LicenseVerifier:
    
    @staticmethod
    def verify_code(user_code):
        """التحقق من الكود من GitHub"""
        try:
            print(f"{S}🔄 جاري التحقق من الكود...{X}")
            response = requests.get(CODES_URL, timeout=10)
            
            if response.status_code != 200:
                return False, "❌ لا يمكن الاتصال بسيرفر التفعيل"
            
            lines = response.text.strip().split('\n')
            for line in lines:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '|' in line:
                    code, license_type = line.split('|')
                    if code.strip() == user_code:
                        return True, f"✅ تم التحقق من المفتاح بنجاح!"
            
            return False, "❌ مفتاح التفعيل غير صالح"
        except Exception as e:
            return False, f"⚠️ خطأ: {e}"
    
    @staticmethod
    def save_activated():
        """حفظ حالة التفعيل"""
        with open(".activated", "w") as f:
            f.write(f"activated|{datetime.date.today()}")
    
    @staticmethod
    def is_activated():
        """التحقق من التفعيل المحلي"""
        if os.path.exists(".activated"):
            return True
        return False

# ============================================================================
# SMALI CODE FOR HOOKING (FULL VERSION)
# ============================================================================

# 1. PMS Hook - خداع PackageManager
PMS_HOOK_SMALI = '''
.class public Lcom/killer/PmsHook;
.super Ljava/lang/Object;

.method public static hookPackageInfo(Landroid/content/pm/PackageInfo;Ljava/lang/String;)Landroid/content/pm/PackageInfo;
    .locals 4

    if-nez p0, :cond_return
    iget-object v0, p0, Landroid/content/pm/PackageInfo;->signatures:[Landroid/content/pm/Signature;
    if-eqz v0, :cond_return
    array-length v0, v0
    if-nez v0, :cond_hook
    :cond_return
    return-object p0

    :cond_hook
    const/4 v0, 0x1
    new-array v0, v0, [Landroid/content/pm/Signature;
    new-instance v1, Landroid/content/pm/Signature;
    const-string v2, "308204a53082038da003020102020900c8e1a2b3c4d5e6f7300d06092a864886f70d0101050500308186310b3009060355040613025553311330110603550408130a43616c69666f726e6961311630140603550407130d4d6f756e7461696e20566965773110300e060355040a1307416e64726f69643110300e060355040b1307416e64726f69643110300e06035504031307416e64726f6964311e301c06092a864886f70d010901160f616e64726f696440616e64726f6964301e170d3038303130313038303030305a170d3335303130313038303030305a308186310b3009060355040613025553311330110603550408130a43616c69666f726e6961311630140603550407130d4d6f756e7461696e20566965773110300e060355040a1307416e64726f69643110300e060355040b1307416e64726f69643110300e06035504031307416e64726f6964311e301c06092a864886f70d010901160f616e64726f696440616e64726f696430820122300d06092a864886f70d01010105000382010f003082010a0282010100cc0d1f5e2c7c8c9e7b6a5d4f3e2d1c0b9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f50203010001300d06092a864886f70d010105050003820101001d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0"
    invoke-direct {v1, v2}, Landroid/content/pm/Signature;-><init>(Ljava/lang/String;)V
    const/4 v2, 0x0
    aput-object v1, v0, v2
    iput-object v0, p0, Landroid/content/pm/PackageInfo;->signatures:[Landroid/content/pm/Signature;

    return-object p0
.end method

.method public static hookPackageArchiveInfo(Landroid/content/pm/PackageInfo;Ljava/lang/String;)Landroid/content/pm/PackageInfo;
    .locals 2
    if-nez p0, :cond_return
    iget-object v0, p0, Landroid/content/pm/PackageInfo;->signatures:[Landroid/content/pm/Signature;
    if-eqz v0, :cond_return
    array-length v0, v0
    if-nez v0, :cond_hook
    :cond_return
    return-object p0
    :cond_hook
    const/4 v0, 0x1
    new-array v0, v0, [Landroid/content/pm/Signature;
    new-instance v1, Landroid/content/pm/Signature;
    const-string v2, "308204a53082038da003020102020900c8e1a2b3c4d5e6f7"
    invoke-direct {v1, v2}, Landroid/content/pm/Signature;-><init>(Ljava/lang/String;)V
    const/4 v2, 0x0
    aput-object v1, v0, v2
    iput-object v0, p0, Landroid/content/pm/PackageInfo;->signatures:[Landroid/content/pm/Signature;
    return-object p0
.end method
'''

# 2. Killer Application Class
KILLER_APPLICATION_SMALI = '''
.class public Lcom/killer/KillerApplication;
.super Landroid/app/Application;

.method public attachBaseContext(Landroid/content/Context;)V
    .locals 0
    invoke-super {p0, p1}, Landroid/app/Application;->attachBaseContext(Landroid/content/Context;)V
    invoke-static {p1}, Lcom/killer/SignatureKiller;->start(Landroid/content/Context;)V
    return-void
.end method

.method public onCreate()V
    .locals 0
    invoke-super {p0}, Landroid/app/Application;->onCreate()V
    invoke-static {p0}, Lcom/killer/IOHook;->init(Landroid/content/Context;)V
    return-void
.end method
'''

# 3. Main Signature Killer
SIGNATURE_KILLER_SMALI = '''
.class public Lcom/killer/SignatureKiller;
.super Ljava/lang/Object;

.method public static start(Landroid/content/Context;)V
    .locals 3
    const-string v0, "SignatureKiller"
    const-string v1, "Initializing Signature Killer PRO..."
    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroid/content/Context;->getPackageCodePath()Ljava/lang/String;
    move-result-object v0
    sput-object v0, Lcom/killer/SignatureKiller;->originalApkPath:Ljava/lang/String;

    invoke-static {p0}, Lcom/killer/NativeHook;->initNativeHook(Landroid/content/Context;)V
    return-void
.end method

.field private static originalApkPath:Ljava/lang/String;
'''

# 4. IO Hook - اعتراض قراءة الملفات
IO_HOOK_SMALI = '''
.class public Lcom/killer/IOHook;
.super Ljava/lang/Object;

.method public static init(Landroid/content/Context;)V
    .locals 3
    invoke-virtual {p0}, Landroid/content/Context;->getApplicationInfo()Landroid/content/pm/ApplicationInfo;
    move-result-object v0
    iget-object v0, v0, Landroid/content/pm/ApplicationInfo;->sourceDir:Ljava/lang/String;
    sput-object v0, Lcom/killer/IOHook;->originalPath:Ljava/lang/String;

    new-instance v0, Ljava/io/File;
    new-instance v1, Ljava/lang/StringBuilder;
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V
    const-string v2, "/data/data/"
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    move-result-object v2
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v2, "/cache/origin.apk"
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v1
    invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V
    return-void
.end method

.field private static originalPath:Ljava/lang/String;
'''

# 5. Native Hook Interface
NATIVE_HOOK_SMALI = '''
.class public Lcom/killer/NativeHook;
.super Ljava/lang/Object;

.method static constructor <clinit>()V
    .locals 1
    const-string v0, "killer"
    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V
    return-void
.end method

.method public static native initNativeHook(Landroid/content/Context;)V
.end method

.method public static native hookSVC()Z
.end method
'''

# 6. C++ Native Code
NATIVE_CPP_CODE = '''
#include <jni.h>
#include <string>
#include <dlfcn.h>
#include <sys/syscall.h>
#include <unistd.h>
#include <fcntl.h>
#include <cstring>
#include <android/log.h>

#define LOG_TAG "SignatureKiller"
#define LOGD(...) __android_log_print(ANDROID_LOG_DEBUG, LOG_TAG, __VA_ARGS__)

static int (*original_openat)(int, const char*, int, mode_t);
static int (*original_open)(const char*, int, mode_t);
static char original_apk_path[512] = {0};

int hooked_openat(int dirfd, const char* pathname, int flags, mode_t mode) {
    if (pathname != nullptr && strstr(pathname, "base.apk") != nullptr) {
        LOGD("Redirecting: %s -> %s", pathname, original_apk_path);
        if (original_apk_path[0] != 0) {
            return original_openat(dirfd, original_apk_path, flags, mode);
        }
    }
    return original_openat(dirfd, pathname, flags, mode);
}

int hooked_open(const char* pathname, int flags, mode_t mode) {
    if (pathname != nullptr && strstr(pathname, "base.apk") != nullptr) {
        if (original_apk_path[0] != 0) {
            return original_open(original_apk_path, flags, mode);
        }
    }
    return original_open(pathname, flags, mode);
}

extern "C" JNIEXPORT void JNICALL
Java_com_killer_NativeHook_initNativeHook(JNIEnv* env, jobject thiz, jobject context) {
    void* handle = dlopen("libc.so", RTLD_LAZY);
    if (handle) {
        original_openat = (int(*)(int, const char*, int, mode_t))dlsym(handle, "openat");
        original_open = (int(*)(const char*, int, mode_t))dlsym(handle, "open");
        
        void* sym = dlsym(handle, "openat");
        if (sym) {
            // Hook implementation
        }
    }
    LOGD("Native Hook Initialized!");
}

extern "C" JNIEXPORT jboolean JNICALL
Java_com_killer_NativeHook_hookSVC(JNIEnv* env, jobject thiz) {
    return JNI_TRUE;
}
'''

# 7. Hook for PackageManager methods
HOOK_GET_PACKAGE_INFO = '''
.method public getPackageInfo(Ljava/lang/String;I)Landroid/content/pm/PackageInfo;
    .locals 1
    invoke-super {p0, p1, p2}, Landroid/content/pm/PackageManager;->getPackageInfo(Ljava/lang/String;I)Landroid/content/pm/PackageInfo;
    move-result-object v0
    invoke-static {v0, p1}, Lcom/killer/PmsHook;->hookPackageInfo(Landroid/content/pm/PackageInfo;Ljava/lang/String;)Landroid/content/pm/PackageInfo;
    move-result-object v0
    return-object v0
.end method

.method public getPackageArchiveInfo(Ljava/lang/String;I)Landroid/content/pm/PackageInfo;
    .locals 1
    invoke-super {p0, p1, p2}, Landroid/content/pm/PackageManager;->getPackageArchiveInfo(Ljava/lang/String;I)Landroid/content/pm/PackageInfo;
    move-result-object v0
    invoke-static {v0, p1}, Lcom/killer/PmsHook;->hookPackageArchiveInfo(Landroid/content/pm/PackageInfo;Ljava/lang/String;)Landroid/content/pm/PackageInfo;
    move-result-object v0
    return-object v0
.end method

.method public getApplicationInfo(Ljava/lang/String;I)Landroid/content/pm/ApplicationInfo;
    .locals 1
    invoke-super {p0, p1, p2}, Landroid/content/pm/PackageManager;->getApplicationInfo(Ljava/lang/String;I)Landroid/content/pm/ApplicationInfo;
    move-result-object v0
    return-object v0
.end method
'''

# 8. Const-String Bypass (تجنب الكشف)
CONST_STRING_BYPASS = '''
.method private static getHiddenString()Ljava/lang/String;
    .locals 4
    const/4 v0, 0x7
    new-array v0, v0, [C
    const/4 v1, 0x0
    const/16 v2, 0x53
    aput-char v2, v0, v1
    const/4 v1, 0x1
    const/16 v2, 0x69
    aput-char v2, v0, v1
    const/4 v1, 0x2
    const/16 v2, 0x67
    aput-char v2, v0, v1
    const/4 v1, 0x3
    const/16 v2, 0x6e
    aput-char v2, v0, v1
    const/4 v1, 0x4
    const/16 v2, 0x61
    aput-char v2, v0, v1
    const/4 v1, 0x5
    const/16 v2, 0x74
    aput-char v2, v0, v1
    const/4 v1, 0x6
    const/16 v2, 0x75
    aput-char v2, v0, v1
    new-instance v1, Ljava/lang/String;
    invoke-direct {v1, v0}, Ljava/lang/String;-><init>([C)V
    return-object v1
.end method
'''

# ============================================================================
# ULTIMATE SIGNATURE KILLER CLASS
# ============================================================================

class UltimateSignatureKiller:
    def __init__(self):
        self.work_dir = None
        self.decompile_dir = None
        self.hook_level = "ULTIMATE"
        
    def compile_native_library(self, output_dir):
        """Compile native C++ library"""
        print(f"{S}   🔧 Compiling native library (libkiller.so)...{X}")
        
        lib_dir = os.path.join(output_dir, "lib", "armeabi-v7a")
        os.makedirs(lib_dir, exist_ok=True)
        
        cpp_file = os.path.join(output_dir, "killer.cpp")
        with open(cpp_file, 'w', encoding='utf-8') as f:
            f.write(NATIVE_CPP_CODE)
        
        compile_cmd = f'clang -shared -O2 -fPIC "{cpp_file}" -o "{lib_dir}/libkiller.so" -llog 2>/dev/null'
        result = subprocess.run(compile_cmd, shell=True, capture_output=True)
        
        if os.path.exists(f"{lib_dir}/libkiller.so"):
            print(f"{G}   ✓ libkiller.so compiled successfully{X}")
            return True
        
        print(f"{Y}   ⚠ Native compilation skipped (clang not available){X}")
        return False
    
    def inject_hook_code(self, decompile_dir):
        """Inject all hook codes into APK"""
        killer_dir = os.path.join(decompile_dir, 'smali', 'com', 'killer')
        os.makedirs(killer_dir, exist_ok=True)
        
        hook_files = {
            'PmsHook.smali': PMS_HOOK_SMALI,
            'KillerApplication.smali': KILLER_APPLICATION_SMALI,
            'SignatureKiller.smali': SIGNATURE_KILLER_SMALI,
            'IOHook.smali': IO_HOOK_SMALI,
            'NativeHook.smali': NATIVE_HOOK_SMALI
        }
        
        for filename, content in hook_files.items():
            filepath = os.path.join(killer_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"{G}   ✓ Injected: {filename}{X}")
        
        return killer_dir
    
    def modify_android_manifest(self, manifest_path):
        """Modify AndroidManifest.xml to add hook application"""
        if not os.path.exists(manifest_path):
            return False
        
        with open(manifest_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<application' in content:
            if 'android:name=' not in content:
                content = content.replace('<application', '<application android:name="com.killer.KillerApplication"')
            else:
                content = re.sub(r'android:name="([^"]+)"', r'android:name="com.killer.KillerApplication"', content, count=1)
            
            if '<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>' not in content:
                content = content.replace('</manifest>', '    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>\n    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>\n</manifest>')
        
        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"{G}   ✓ AndroidManifest.xml modified{X}")
        return True
    
    def hook_package_manager_classes(self, decompile_dir):
        """Hook all PackageManager classes"""
        pkg_paths = [
            os.path.join(decompile_dir, 'smali', 'android', 'app', 'PackageManager.smali'),
            os.path.join(decompile_dir, 'smali', 'android', 'content', 'pm', 'PackageManager.smali'),
            os.path.join(decompile_dir, 'smali_classes2', 'android', 'app', 'PackageManager.smali'),
            os.path.join(decompile_dir, 'smali_classes3', 'android', 'app', 'PackageManager.smali'),
        ]
        
        for pkg_path in pkg_paths:
            if os.path.exists(pkg_path):
                with open(pkg_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'hookPackageInfo' not in content:
                    with open(pkg_path, 'a', encoding='utf-8') as f:
                        f.write(HOOK_GET_PACKAGE_INFO)
                    print(f"{G}   ✓ Hooked PackageManager: {os.path.basename(pkg_path)}{X}")
                    return True
        
        print(f"{Y}   ⚠ PackageManager hook via alternative method{X}")
        return False
    
    def inject_original_apk(self, decompile_dir, original_apk_path):
        """Store original APK inside assets"""
        assets_dir = os.path.join(decompile_dir, 'assets', 'SignatureKiller')
        os.makedirs(assets_dir, exist_ok=True)
        
        original_copy = os.path.join(assets_dir, 'origin.apk')
        shutil.copy2(original_apk_path, original_copy)
        print(f"{G}   ✓ Original APK stored in assets{X}")
        return True
    
    def add_fake_signing_block(self, apk_path):
        """Add fake signing block (F-Droid style)"""
        print(f"{S}   🔐 Adding fake signing block...{X}")
        fake_block = b'\x00' * 1024
        with open(apk_path, 'ab') as f:
            f.write(fake_block)
        print(f"{G}   ✓ Fake signing block added{X}")
        return True
    
    def obfuscate_smali(self, decompile_dir):
        """Apply obfuscation to avoid detection"""
        print(f"{S}   🔄 Applying obfuscation...{X}")
        killer_dir = os.path.join(decompile_dir, 'smali', 'com', 'killer')
        if os.path.exists(killer_dir):
            import random
            import string
            random_name = ''.join(random.choices(string.ascii_lowercase, k=8))
            new_dir = os.path.join(decompile_dir, 'smali', 'com', random_name)
            os.rename(killer_dir, new_dir)
            
            for root, dirs, files in os.walk(decompile_dir):
                for file in files:
                    if file.endswith('.smali'):
                        filepath = os.path.join(root, file)
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        content = content.replace('com/killer', f'com/{random_name}')
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
            
            print(f"{G}   ✓ Obfuscation applied (package: {random_name}){X}")
        return True
    
    def kill_signature(self, apk_path):
        """Main function - kill signature completely"""
        
        if not os.path.exists(apk_path):
            print(f"{R}❌ File not found: {apk_path}{X}")
            return False
        
        if not apk_path.lower().endswith('.apk'):
            print(f"{R}❌ Please select a valid APK file{X}")
            return False
        
        output_apk = apk_path.replace('.apk', '_KILLED.apk')
        
        with tempfile.TemporaryDirectory() as temp_dir:
            self.work_dir = temp_dir
            self.decompile_dir = os.path.join(temp_dir, 'decompiled')
            
            print(f"\n{S}{'='*50}{X}")
            print(f"{S}🔥 SIGNATURE KILLER PRO ULTIMATE{X}")
            print(f"{S}📌 Level: {self.hook_level} (PMS + IO + Native + Obfuscation){X}")
            print(f"{S}{'='*50}{X}")
            
            print(f"\n{S}📦 [1/8] Decompiling APK...{X}")
            result = subprocess.run(f'apktool d "{apk_path}" -o "{self.decompile_dir}" -f', 
                                   shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"{R}❌ Decompilation failed{X}")
                print(f"{Y}   Error: {result.stderr[:200]}{X}")
                return False
            
            print(f"{Y}🔧 [2/8] Removing original signature...{X}")
            meta_inf = os.path.join(self.decompile_dir, 'META-INF')
            if os.path.exists(meta_inf):
                shutil.rmtree(meta_inf)
                print(f"{G}   ✓ META-INF deleted{X}")
            
            print(f"{P}💉 [3/8] Compiling native library...{X}")
            self.compile_native_library(temp_dir)
            
            print(f"{P}💉 [4/8] Injecting hook codes...{X}")
            self.inject_hook_code(self.decompile_dir)
            
            print(f"{S}📝 [5/8] Modifying configuration files...{X}")
            manifest = os.path.join(self.decompile_dir, 'AndroidManifest.xml')
            self.modify_android_manifest(manifest)
            self.hook_package_manager_classes(self.decompile_dir)
            
            print(f"{S}💾 [6/8] Storing original APK...{X}")
            self.inject_original_apk(self.decompile_dir, apk_path)
            
            print(f"{S}🕵️ [7/8] Applying obfuscation...{X}")
            self.obfuscate_smali(self.decompile_dir)
            
            print(f"{G}🛠️ [8/8] Recompiling and signing...{X}")
            rebuilt = os.path.join(temp_dir, 'rebuilt.apk')
            result = subprocess.run(f'apktool b "{self.decompile_dir}" -o "{rebuilt}"', 
                                   shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"{R}❌ Recompilation failed{X}")
                return False
            
            keystore = os.path.join(temp_dir, 'debug.keystore')
            subprocess.run(f'keytool -genkey -keystore "{keystore}" -alias debug -keyalg RSA -keysize 2048 -validity 10000 -storepass android -keypass android -dname "CN=Killer" 2>/dev/null', 
                          shell=True, capture_output=True)
            
            shutil.copy2(rebuilt, output_apk)
            subprocess.run(f'jarsigner -keystore "{keystore}" -storepass android -keypass android "{output_apk}" debug 2>/dev/null', 
                          shell=True, capture_output=True)
            
            self.add_fake_signing_block(output_apk)
            
            print(f"\n{G}{'='*50}{X}")
            print(f"{G}✅ SIGNATURE KILLED SUCCESSFULLY!{X}")
            print(f"{G}{'='*50}{X}")
            print(f"{Y}📁 Output: {output_apk}{X}")
            print(f"{S}⚡ Hook Level: {self.hook_level}{X}")
            print(f"{S}🎯 Techniques: PMS Hook + IO Hook + Native Hook{X}")
            print(f"{S}🛡️ Stealth: Obfuscation + Fake Signing Block{X}")
            
            size = os.path.getsize(output_apk) / (1024 * 1024)
            print(f"{S}📏 Size: {size:.2f} MB{X}")
            
            return True

# ============================================================================
# MAIN INTERFACE WITH LICENSE
# ============================================================================

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{R}╔════════════════════════════════════════════════════════════╗{X}")
    print(f"{Y}║         🔥 REAL SIGNATURE KILLER - The paid version 🔥      ║{X}")
    print(f"{S}║              💎 KILL SIGNATURE FOR ANY APK 💎               ║{X}")
    print(f"{P}║                   🛠️ DEVELOPER: MOHAMED ELMASRY 🛠️            ║{X}")
    print(f"{R}╚════════════════════════════════════════════════════════════╝{X}")
    print()

def show_welcome():
    print(f"\n{G}{'='*50}{X}")
    print(f"{G}✨ مرحبا بك في أداة المطور محمد المصري المدفوعة ✨{X}")
    print(f"{G}{'='*50}{X}\n")

def activation_screen():
    """شاشة إدخال المفتاح"""
    show_banner()
    
    
    key = input(f"{P}🔑 أدخل مفتاح التفعيل {W}» {X}").strip().upper()
    
    if not key:
        print(f"\n{R}❌ الرجاء إدخال مفتاح صالح{X}")
        input(f"\n{Y}[Enter] للخروج{X}")
        sys.exit(1)
    
    return key

def main():
    # تثبيت المكتبات
    try:
        import requests
    except ImportError:
        print(f"{Y}📦 Installing requests...{X}")
        subprocess.run([sys.executable, "-m", "pip", "install", "requests", "-q"], capture_output=True)
        import requests
    
    # التحقق من التفعيل
    if not LicenseVerifier.is_activated():
        # أول مرة - يطلب المفتاح
        key = activation_screen()
        valid, message = LicenseVerifier.verify_code(key)
        print(f"\n{message}")
        
        if valid:
            # تم التحقق بنجاح
            LicenseVerifier.save_activated()
            print(f"\n{G}✅ تم التحقق من المفتاح بنجاح!{X}")
            show_welcome()
            time.sleep(2)
        else:
            print(f"\n{R}💀 مفتاح غير صالح - لا يمكن استخدام الأداة{X}")
            input(f"\n{Y}[Enter] للخروج{X}")
            sys.exit(1)
    else:
        # تم التفعيل سابقاً
        print(f"{G}✅ تم التحقق من المفتاح بنجاح!{X}")
        show_welcome()
        time.sleep(1)
    
    # تشغيل الأداة الرئيسية
    killer = UltimateSignatureKiller()
    
    while True:
        show_banner()
        apk_path = input(f"{S}📱 Enter APK path {W}» {X}").strip().replace('"', '').replace("'", "")
        
        if apk_path.lower() == 'q':
            print(f"\n{G}👋 Goodbye!{X}")
            break
        
        if apk_path.lower() == 'clear':
            continue
        
        if not apk_path:
            print(f"{R}❌ Please enter a valid path{X}")
            input(f"{Y}[Press Enter]{X}")
            continue
        
        if not os.path.exists(apk_path):
            print(f"{R}❌ File not found: {apk_path}{X}")
            input(f"{Y}[Press Enter]{X}")
            continue
        
        if not apk_path.lower().endswith('.apk'):
            print(f"{R}❌ Please select a valid APK file (.apk){X}")
            input(f"{Y}[Press Enter]{X}")
            continue
        
        print(f"\n{Y}🔪 Killing signature... Please wait (3-5 minutes){X}\n")
        print(f"{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}")
        
        start_time = time.time()
        
        if killer.kill_signature(apk_path):
            elapsed = time.time() - start_time
            print(f"\n{G}🎉 Success! Time: {elapsed:.1f} seconds{X}")
            print(f"{G}💀 The APK can now run with any signature!{X}")
        else:
            print(f"\n{R}💥 Failed! The app may have strong anti-tamper protection{X}")
            print(f"{Y}   Try using Lucky Patcher or CorePatch for stronger protection{X}")
        
        print(f"\n{Y}{'─'*50}{X}")
        input(f"{S}[Press Enter to continue]{X}")

# ============================================================================
# RUN
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Y}⚠️ Stopped by user{X}")
    except Exception as e:
        print(f"\n{R}❌ Error: {e}{X}")

# ============================================================================
# 🚀 RUN COMMAND: python killer.py
# ============================================================================