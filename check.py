print("導入されているpythonのバージョンをチェックします。\n")

import sys, platform

print("プログラムが想定しているPythonバージョン: 3.6.x")
print("コンピューターにインストール済みのPython: {0}\n".format(platform.python_version()))

if sys.version_info[0] == 3:
    if sys.version_info[1] == 6:
        if sys.version_info[2] == 5:
            print("動作環境は完璧です！")
        else:
            print("動作環境に問題はありません。")
        deal = "perfect"
    else:
        print("ほとんどの機能は動作しますが、一部機能が動作しない可能性があります。")
        print("python 3.6.5へ変更することを推奨します。")
        deal = "good"
else:
    print("python2ではBOTプログラムを動かすことができません。")
    print("python3で動作するようにしてください。推奨は3.6.5です。")
    print("導入したら再度'python check.py'を実行してください")
    sys.exit(1)

print("\n--------------------------------------------------------------------\n")

print("必要なライブラリがインストールされているかチェックします\n")

print("discord.py")
try:
    import discord
    print("  正常にインストールされています。")
except ImportError:
    print("  インポート失敗。")
    print("'pip install discord.py'を実行し、インストールしてください。'")
except Exception as e:
    print("想定外のエラー:")
    print(e)
    sys.exit(1)

print("schedule")
try:
    import schedule
    print("  正常にインストールされています。")
except ImportError:
    print("  インポート失敗。")
    print("'pip install schedule'を実行し、インストールしてください。'")
except Exception as e:
    print("想定外のエラー:")
    print(e)
    sys.exit(1)

if deal == "perfect":
    print("""
    +------------------------------------+
    |          Congratulation!           |
    |すべての設定が完璧に行われています！|
    +------------------------------------+
    """)
else:
    print("""
    +-----------------------------------------------+
    |                     Good!                     |
    |pythonのバージョンの修正まで行えるとperfectです！|
    +-----------------------------------------------+
    """)
