import unreal
import sys

# 引数をVectorに保存
offset = unreal.Vector(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))

# エディタ上で選択されているアクターを取得
actors = unreal.EditorLevelLibrary.get_selected_level_actors()
for actor in actors:

    # 現在選択されているアクター
    target_actor = actor

    # 現在の位置を取得
    current_location = target_actor.get_actor_location()

    # 位置を引数の値加算する
    new_location = current_location + offset

    # 新しい位置を設定
    target_actor.set_actor_location(new_location, False, True)
    print(f"{target_actor.get_name()} の位置を {new_location} に更新しました")