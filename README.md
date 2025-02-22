# problem-template-python

## はじめに

Problem Template Pythonは、PythonでOptHubの問題を作成するためのテンプレートリポジトリです。以下の手順に従って、問題を作成してください。

## 手順

### 1. 事前準備

- Python 3.10以上をインストール

### 2. プロジェクトの設定

1. 本リポジトリをclone
2. Poetryを設定
    - 推奨バージョン:Poetry 1.8.x
3. `example_problem`ディレクトリの名前を問題名に変更
    - スネークケースを用いてください。 例:`number_place`
4. `Dockerfile`を編集
    - 3.で設定したディレクトリ名を用いて、`Dockerfile`を以下のように編集してください。

        ```Dockerfile
        # Run the command (modify here)
        CMD ["sh", "-c", "cd /usr/src/app && poetry run python ./(3.で設定したディレクトリ名)/main.py"]
        ```

5. `Makefile`を編集
    - `Makefile`の`NAME`に問題名を設定してください。

6. `pyproject.toml`を編集
    - `pyproject.toml`には、プロジェクトのメタデータの一例が入力されています。ファイルを編集し、問題名や依存パッケージ、著者情報等を適切に入力してください。
7. ライセンスを編集
    - `LICENSE`ファイルを編集し、適切なライセンスを設定してください。デフォルトはMITライセンスを設定しています。

### 3. 環境変数の追加

環境変数は、最適化対象の関数を具体的に決定するためのパラメータです。異なる環境変数を設定することで、一つの問題から複数の異なる競技を作成することができます。

以下の手順で`example_problem/main.py`を編集し、環境変数を追加してください。

1. `example_problem/main.py`の`main`関数の引数`example_env`を、環境変数の名前に変更
2. 1.で設定した環境変数に対して、`@click.option`を作成し、デフォルト値等を設定
    - Optionsの使い方は[こちら](https://click.palletsprojects.com/en/stable/options/)を参照してください。

複数の環境変数を追加することも可能です。複数の環境変数を設定する場合には、`main`関数の引数に各環境変数を設定し、それぞれに対して`@click.option`を作成してください。

### 4. 評価関数の作成

評価関数は、ユーザから送信された解を評価して、目的関数、制約関数、実行可能性、付随情報を返却する関数です。

以下の手順で、`example_problem/evaluator`ディレクトリに評価関数を実装し、`example_problem/evaluator/main.py`の`evaluate`関数を用いて評価結果が得られるようにします。

1. `evaluate`関数の入力に、解(`variable`)と、[3.環境変数の追加](#3-環境変数の追加)で追加した環境変数を設定
2. `evaluate`関数に、評価のロジックを実装
3. `evaluate`関数の出力(評価結果)に、以下のキーを持つdictを設定

    | キー | 型 | 説明 | 必須か |
    | -------- | -------- | -------- | -------- |
    | `objective`  | `float` \| `list[float]` | 目的関数値 | **必須** |
    | `constraint` | `float` \| `list[float]` | 制約関数値 | 任意 |
    | `feasible` | `bool` | 実行可能性 | 任意 |
    | `info` | `object` | 付随情報 |　任意 |

### 5. 解/環境変数を検証する関数の作成

`example_problem/validators`ディレクトリに、解/環境変数の形式を検証し、検証済みの解/環境変数を返す関数を作成します。検証は、[JSON Schema](https://json-schema.org/)を用いて実装できます。JSON Schemaの作成方法は[こちら](https://json-schema.org/understanding-json-schema/basics)を参照してください。

#### 5.1 解を検証する関数の作成　（`example_problem/validators/variable.py`）

1. 解を検証するためのスキーマを作成
    - 1つのスキーマにまとめることが難しければ、後述の`validate_variable`関数内で、複数のスキーマを組み合わせることも可能です。
2. `jsonschema`の`validate`関数を用いて、ユーザが送信した解を検証する関数`validate_variable`を実装

#### 5.2 環境変数を検証する関数`validate_(環境変数名)`の作成 (`example_problem/validators/(環境変数名).py`)

1. `example_problem/validators/example_env.py`のファイル名を、[3.環境変数の追加](#3-環境変数の追加)で追加した環境変数名を用いて`example_problem/validators/(環境変数名).py`に変更*
2. 環境変数を検証するためのスキーマを作成
    - 1つのスキーマにまとめることが難しければ、後述の`validate_(環境変数名)`関数内で、複数のスキーマを組み合わせることも可能です。
3. `jsonschema`の`validate`関数を用いて、環境変数を検証する関数`validate_(環境変数名)`を実装

*複数の環境変数を追加した場合は、複数のファイルを作成し、それぞれの環境変数を検証する関数を実装してください。

#### 解の検証のガイドライン

検証の原則はシンプルです。

- 探索空間内の解をすべて受け入れます（実行可能解だけでなく、実行不可能解も受け入れます）。
- それ以外は何も受け入れてはいけません。

問題がどんな解を受け入れるかは検証によって決まります。
言い換えれば、検証とは数学的な探索空間（目的関数と制約関数の定義域）を計算機上で実装したものです。

コンペティションの参加者は、検証をパスする解を「ルール上認められた合法手」とみなし、許容範囲ギリギリまで探索しようとします。
どんな解が検証をパスするかによって、コンペティションの結果も左右されます。
作問者は、参加者の創意工夫を妨げないように、数学的に許容される解はできるかぎりすべて検証をパスするように実装してください。

一方で、想定外の解を受け入れないことも重要です。
Web APIの性質上、参加者はどんなデータでも送ることができます（文字通り、あらゆるビット列を送信できます）。
問題プログラムを不正な入力から守るために、データ型のチェックはもちろん、余分なプロパティを含んだり不足するプロパティがある場合には拒否し、変数の最大値と最小値や配列の長さも必要十分な範囲に制限してください。
制限が甘いと、1TBのデータを読み込んでサーバーがダウンしたり、1000桁の数値を読み込んでオーバーフローした評価値を返してしまい、コンペティションの中断ややり直しを招く可能性があります。

もちろん現実には、JSON Schemaの表現力には限界があり、数学的な探索空間を忠実に実装できるとは限りません。
しかし、ここでできるかぎり理想を目指しておくのがトータルで見れば最も安上がりです。
検証がしっかりしていると、問題プログラムの中では値のチェックを簡単に済ませることができ、コンペティション中のトラブルが減ります。

### 6. main関数の修正

[3.環境変数の追加](#3-環境変数の追加)から[5.解/環境変数を検証する関数の作成](#5-解環境変数を検証する関数の作成)で作成した関数を用いるため、`example_problem/main.py`の`main`関数を修正します。

- `example_env`の例を参考に、追加した環境変数を検証してください。
- `evaluate`関数の引数に、追加した環境変数を設定してください。

### 7. テストの作成

`tests`ディレクトリ下に、実装した各種関数を検証するテストコードを作成します。以下に関して、テストコードを作成してください。

- 評価関数 (`tests/evaluator`ディレクトリ)
- 解と環境変数の検証関数 (`tests/validators`ディレクトリ)
- これらの関数の統合テスト (`tests/test_main.py`)

統合テストでは、作成した問題のDocker Imageをbuildし、[opthub-runner-python](https://github.com/opthub-org/opthub-runner-python)を使って評価をテストしています。

このテンプレートでは、pytestを用いてテストを実装しています。テスト用のファイル及び関数は、test_(テスト対象の関数やファイル名)で命名することに注意してください。

以下のコマンドを実行することで、`tests`ディレクトリ下に作成したテストをすべて実行することができます。

```plaintext
make test
```

#### 数値計算のテストについてのガイドライン

ここでは、典型的なコーナーケースとそのテスト方法について説明します。

数値計算には浮動小数点数のコーナーケースにまつわる落とし穴が大量にあります。
コンペティションではスコアを最大化/最小化するためにギリギリを攻めることになるので、そういったコーナーケースを踏みやすいです。
そのため、普段は問題なく動作していたプログラムが、コンペティション本番中に予期しない動作を起こすことがしばしばあります。

**基本的な考え方**

- (悪意のある) 攻撃者の視点に立って、プログラムを壊す/穴を突く方法を考える。
- 正常値と異常値の境界を探し、境界ギリギリの内側/外側の値をテストする。
- エラーが出力されるケースを探し、エラー出力が別の問題を引き起こさないか確認する。

**重要度：テストすべきこと**

1. 高：入出力に`NaN`を含むケース
2. 高：入出力に`null`を含むケース (nullableな場合)
3. 高：入出力に`+inf`や`-inf`を含むケース
4. 高：エラーコード代わりに特別な数を返すケース (特に`0`、`-1`、`+inf`、`-inf`、`NaN`に注意)
5. 中：`+0.0`と`-0.0`を区別しなければならないケース
6. 中：非決定計算による結果の変動 (マルチスレッド、GPU、分散処理)
7. 低：とても大きな数ととても小さな数の演算 (丸め誤差)
8. 低：`abs(f(x) - f(x + dx)) < eps`になっているか (連続関数の場合)

### 8. ログ出力の設定

ログに実行時情報を記録し、追跡しやすくします。

このテンプレートでは、`example_problem/main.py`でログが取られています。

```python
LOGGER = logging.getLogger(__name__) # Logger
```

`logging`について、詳しくは[こちら](https://docs.python.org/3.13/howto/logging.html)等を参照してください。

### 9. CI/CD (任意)

`git push`した際に、Docker Imageを自動でbuildして公開できるように、CI/CDの設定を行います。`DOCKER_USERNAME`と`DOCKER_PASSWORD`をGitHub ActionsのSecret Variablesに設定してください。

## FAQ

### どのようにしてLinterを無効にしますか

以下を`pyproject.toml`に追記し、Linterを無効化したいディレクトリを指定してください。

```pyproject.toml
[tool.ruff]
︙
lint.exclude = [
    "example_problem/*", 
]
```

### Pythonだけでは動作しないパッケージがある場合、どうすればよいですか

`Dockerfile`を編集して、環境構築を行なってください。Pythonパッケージの中には、`pypandoc`等、Pythonだけでは動作しない依存関係を必要とするものがあります。このようなパッケージを扱う場合には、Docker内に外部ライブラリやツールをインストールする必要があります。

## お問い合わせ

ご質問やご不明な点がございましたら、お気軽にお問い合わせください (Email: dev@opthub.ai)。

<img src="https://opthub.ai/assets/images/logo.svg" width="200">

