import bpy

translation_dict = {
    "ja_JP": {
        ("*", "Path Deform"): "パスで変形",
        ("Operator", "Path Deform"): "パスで変形",
        ("Operator", "Quick"): "即時",
        ("*", "Deforms an edge loop with a curve"): "カーブでエッジループを変形します",
        ("*", "Omit the option for instant transformation"): "オプションを省略して即時変形します",
        ("*", "Control Points"): "制御点",
        ("*", "Confirmed"): "確定しました",
        ("*", "Auto Density"): "密度を自動調整",
        ("*", "Automatically adjust control point distribution based on edge density"): "エッジの密度に基づいて制御点の分布を自動的に調整します",

        # GPU GUI
        ("*", "🐻Tips"): "🐻Tips",
        ("*", "[Click] Confirm"): "[Click] 確定",
        ("*", "[Shift+Wheel] Control Points [Ctrl+Click] Add or Delete [↑↓] Roundness"): "[Shift+ホイール] ポイント数 [Ctrl+クリック] 追加or削除 [↑↓] 曲線の強さ",
        ("*", "[R] Reset Deform [M] Mirror Toggle [H] Hide Path"): "[R] 変形リセット [M] ミラー切り替え [H] パスを非表示",
    }
}  # fmt: skip


def register():
    bpy.app.translations.register(__package__, translation_dict)


def unregister():
    bpy.app.translations.unregister(__package__)
