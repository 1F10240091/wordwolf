# モデルの定義
---

## User（カスタムユーザーモデル）
Django 標準の `AbstractUser` を継承しており、認証機能に加えて以下のゲーム用プロフィール情報を保持します。

- `win_num`: 勝利数  
- `lose_num`: 敗北数  

アプリ全体でこのモデルをユーザーとして使用するため、`AUTH_USER_MODEL` を設定しています。

---

##  WordSet（お題のセット）
ワードウルフの「市民用の単語」と「狼用の単語」のセットを管理するモデルです。

- `main_word`: 市民側のワード  
- `wolf_word`: 狼側のワード  
- `category`: 任意の分類（テーマ管理用）

Room はこの WordSet を 1 つ選択して使用します。

---

## Question（ランダムに出題する質問）
ゲーム中にプレイヤーへ提示される質問を管理するモデルです。

- `text`: 質問文  
- `category`: お題のカテゴリや種別に合わせる場合に使用

Room ではこの中から 3 つを選び、`RoomQuestion` を通じて紐づけます。

---

## Room（ゲームルーム）
プレイヤーが参加してゲームを行う部屋を表すモデルです。

主なフィールド：

- `room_name`：部屋名  
- `max_user_num`：最大参加人数  
- `status`：  
  - `waiting`: 待機中  
  - `playing`: ゲーム中  
  - `finished`: 終了  
- `word_set`：この部屋で使うお題  
- `is_full`（property）：最大人数に達したかどうか  
  → 動的に判断するため DB には保存しません

関連：

- `members`: Room に紐づく Member の一覧  
- `questions`: RoomQuestion で紐づいた 3 つの質問

---

## Member（部屋に参加しているプレイヤー）
Room 内における各プレイヤーの状態を表します。

- `user`: 参加者  
- `room`: 所属している部屋  
- `role`:  
  - `wolf` : 狼  
  - `citizen` : 市民  
- `word`: 各メンバーに配られたワード  
- `vote_target`: 投票対象の別 Member  
- `joined_at`: 入室時間（ログ用途）

---

## RoomQuestion（部屋と質問の中間テーブル）
Room で使用する 3 つの質問を「順序付き」で紐づけるためのモデルです。

- `order`: 1〜3 の順番を保持  
- `room`: 対象となるルーム  
- `question`: 出題される質問