---
layout: post
title: "勝手に編集後記 vol.1"
date: 2022-12-02
last_modified_at: 2022-12-02
categories: [mad]
tags: [tech]
image: "https://github.com/SehataKuro/SehataKuro.github.io/blob/main/madcommentary/%E3%82%B5%E3%82%A4%E3%83%88%E7%94%A8%E3%82%B5%E3%83%A0%E3%83%8D%E3%82%A4%E3%83%AB.png"
description: "この企画は、普段見ている動画の表現の疑問を受け付けて、勝手に編集後記を書くことで解決しよう！という企画です。"
---

この記事は音MAD Advent Calendar 2022に参加しています！

この企画は、普段見ている動画の表現の疑問を受け付けて、勝手に編集後記を書くことで解決しよう！という企画です。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">【お知らせ】<br>音MADを見ているときに、この表現どうやって作ってるんだろう？と思うことはないですか？<br>疑問に思ってもどうやって調べたらいいのかわからなくて詰んでいるものもあると思います。<br>そこで、私の生放送で一緒に動画を見ながら再現や解説をする企画をやろうと思います！</p>&mdash; せはた (@SehataKuro) <a href="https://twitter.com/SehataKuro/status/1578355690607087617?ref_src=twsrc%5Etfw">October 7, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

このツイートで募集した質問をもとに、記事にまとめました！

（書く内容が思いつかなかったとかじゃないですよ！）



↓↓↓↓この記事がよかったらツイッターで共有してください！

<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false">Tweet</a>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

***

## 目次

- [目次](#目次)
- [背景にある六角形のトンネル空間みたいな図形の作り方(マーシャル・バトルドーマー)](#背景にある六角形のトンネル空間みたいな図形の作り方マーシャルバトルドーマー)
  - [- 無限に六角形が出てくる](#--無限に六角形が出てくる)
  - [- 少しづつ角度が変わる](#--少しづつ角度が変わる)
  - [- 速度が手前に来るほど速くなる](#--速度が手前に来るほど速くなる)
  - [- 解像度が荒い](#--解像度が荒い)
- [hacococoさんの動画特有の光や色調と絶妙なボカシやブラーってどうやればできるんでしょうか？(hacococo)](#hacococoさんの動画特有の光や色調と絶妙なボカシやブラーってどうやればできるんでしょうかhacococo)
- [背景の四角形のレイアウトを大小するやり方(Disco Necropolis【合作単品】)](#背景の四角形のレイアウトを大小するやり方disco-necropolis合作単品)
- [「4」の単音だけで人力(きゅうくらよん)](#4の単音だけで人力きゅうくらよん)
- [鳴き声のみで大まかな人力をどのように行っているか(黒白世代宛て図鑑)](#鳴き声のみで大まかな人力をどのように行っているか黒白世代宛て図鑑)
- [「急転相まって壊したって」のフォントが知りたい(～にょろにょろ合作3～【合作単品】)](#急転相まって壊したってのフォントが知りたいにょろにょろ合作3合作単品)
- [堕ちる堕ちるでいっぱい文字でてくるとこ、最後のトラックメイカーの文字出し(インドア系ならマキシマイザー)](#堕ちる堕ちるでいっぱい文字でてくるとこ最後のトラックメイカーの文字出しインドア系ならマキシマイザー)
- [顔面が宇宙人のようになる部分(Big Brother☆.NYD2019【合作単品】)](#顔面が宇宙人のようになる部分big-brothernyd2019合作単品)
- [0:58の後ろにある四角形4つが消える箇所，1:01の画面下右側から飛び出した三角形が細かい三角形になり消える箇所(柴又で学ぶ音MAD映像☆)](#058の後ろにある四角形4つが消える箇所101の画面下右側から飛び出した三角形が細かい三角形になり消える箇所柴又で学ぶ音mad映像)
- [シャロ、サターニャ、しまりんが映るウィンドウの出し方(Big Brother)](#シャロサターニャしまりんが映るウィンドウの出し方big-brother)
- [影莉央さんのキャラクターの良さを引き出すような歌詞改変やセリフ合わせ(影莉央)](#影莉央さんのキャラクターの良さを引き出すような歌詞改変やセリフ合わせ影莉央)
- [きれいに白黒にする方法(？/葉月味)](#きれいに白黒にする方法葉月味)
- [おわりに](#おわりに)

***

## 背景にある六角形のトンネル空間みたいな図形の作り方(マーシャル・バトルドーマー)

<script type="application/javascript" src="https://embed.nicovideo.jp/watch/sm40115538/script?w=640&h=360&from=81"></script><noscript><a href="https://www.nicovideo.jp/watch/sm40115538?from=81">マーシャル・バトルドーマー</a></noscript>

Aviutlを使ってこの図形の再現を解説します。

この図形の大きな特徴は

- 無限に六角形が出てくる
- 少しづつ角度が変わる
- 速度が手前に来るほど速くなる
- 解像度が荒い

の4つです。

この特徴を踏まえたうえで、実際に作っていきたいと思います。

あくまで勝手な再現なので、多少の違いがありますがご容赦ください。

### - 無限に六角形が出てくる

もしあの動画の図形を再現するときに、普通に図形オブジェクトを置くととんでもない数の図形を置くことになります。

書き出しも時間がかかるしなにより手間がかかるのでそれはあまりやりたくありません。

なので、パーティクルを使って効率的に作ろうと思います。

今回はrikkyさんのパーティクル(R)を使います。

[https://hazumurhythm.com/wev/amazon/?script=パーティクルRBa6](https://hazumurhythm.com/wev/amazon/?script=%E3%83%91%E3%83%BC%E3%83%86%E3%82%A3%E3%82%AF%E3%83%ABRBa6)

このスクリプトは、パーティクル本体と拡張用スクリプトの二つを追加することで操作ができます。詳しくはさつきさんのブロマガを参照してください。

[https://site.nicovideo.jp/ch/userblomaga_thanks/archive/ar715342](https://site.nicovideo.jp/ch/userblomaga_thanks/archive/ar715342)

まず、**図形オブジェクトの六角形を追加し、サイズを150、ライン幅を1にします。**

**アニメーション効果から、パーティクル本体と方向と格子を追加します。**

[![img](/madcommentary/MarshallBattleDomer_BG_1.png)](/madcommentary/MarshallBattleDomer_BG_1.png)

### - 少しづつ角度が変わる

今はまだデフォルトの状態です。

デフォルトでは角度の初期値がランダムになっています。

**パーティクル本体の設定をクリックし、各xyz回転初期値を**

**{0,0,r}　から　{0,0,0}　に変更します。**

また、回転の向きや速度を合わせるために、**各xyz回転速度を**

**{0,0,60}　から　{0,0,-90}　に変更します。**

付け加えて、最終的な見栄えをよくするために、**透過率{始、終}を**

**{100,50}　から　{50,100}　に変更します。**

[![img](/madcommentary/MarshallBattleDomer_BG_2.png)](/madcommentary/MarshallBattleDomer_BG_2.png)

### - 速度が手前に来るほど速くなる

この動画の図形は、最初はゆっくりでだんだん速くなっていますね。

この「最初はゆっくりでだんだん速くなっていく現象」で有名なものがありますよね。

そう、自由落下です。つまり重力の力。

今回は、方向と格子のz重力というパラメーターを利用して、だんだん速くなる動きを再現します。

また、z軸なので自動的に手前になるにつれて図形が大きく見えます。

まずは、**方向と格子のz重力を**

**0.0　から　-350.0　にします。**

そして、初速度を0にするために、**パーティクル本体の出力速度を**

**100.00　から　0.00　にします。**

[![img](/madcommentary/MarshallBattleDomer_BG_3.png)](/madcommentary/MarshallBattleDomer_BG_3.png)

急にそれっぽくなってきた。

しかし、少し動きが単調なので回転を入れておきましょう。

私は**1分で8周するくらいの回転**を入れました。

### - 解像度が荒い

**フレームバッファを追加して、アニメーション効果からモザイクを追加し、サイズを3にします。**

さらに**アニメーション効果から、二値化できるスクリプトを追加し、閾値をお好みで調整します。**

私が二値化で使っているスクリプトはティムさんの色調調整セットver6かてつ(XIAO)さんのOpenCVアニメーションスクリプトです。

話は逸れますが、この二つのスクリプトは使いやすく画像処理の基本的な機能がまとまっているので入れておくと便利です。

<iframe width="312" height="176" src="https://ext.nicovideo.jp/thumb/sm35722623" scrolling="no" style="border:solid 1px #ccc;" frameborder="0"><a href="https://www.nicovideo.jp/watch/sm35722623">【AviUtl】 色調調整セットver6</a></iframe>

<iframe width="312" height="176" src="https://ext.nicovideo.jp/thumb/sm32520048" scrolling="no" style="border:solid 1px #ccc;" frameborder="0"><a href="https://www.nicovideo.jp/watch/sm32520048">【Aviutlスクリプト】OpenCVアニメーションスクリプト</a></iframe>

[![img](/madcommentary/MarshallBattleDomer_BG_4.png)](/madcommentary/MarshallBattleDomer_BG_4.png)

中心の部分に動画の図形にはない、円のようなものができています。

これを消すために**図形オブジェクトの円を重ねます。**

**サイズは170で黒色にし、フレームバッファと六角形の間のレイヤーに挟みます。**

[![img](/madcommentary/MarshallBattleDomer_BG_5.png)](/madcommentary/MarshallBattleDomer_BG_5.png)

これで完成です。

あとはこれを書き出してたり、この工程をシーンで行ったりして素材にして、ルミナンスキーを使って黒色を透過すれば、あの動画のような図形が作れると思います。

上の工程がめんどくさい人向けに、プロジェクトファイルと1分耐久の素材を配布します。自由に使ってください。

[MarshallBattleDomer_BG.aup](/madcommentary/MarshallBattleDomer_BG.aup)

<video controls width="100%" autoplay loop muted="true" src="/madcommentary/MarshallBattleDomer_BG.mp4" type="video/mp4" >
 Sorry, your browser doesn't support embedded videos.
</video>

## hacococoさんの動画特有の光や色調と絶妙なボカシやブラーってどうやればできるんでしょうか？(hacococo)

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            hacococoさんの動画特有の光や色調と絶妙なボカシやブラーってどうやればできるんでしょうか？
            <br>
            使用ソフトや工程、意識していることなどについて教えてください！
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_hacocone.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            特有というか完全に癖でやってることなんですが、VegasProのエフェクト「ソフトコントラスト」「明るさとコントラスト」「HitFilm Bleach Bypass」「ホワイトグロウ」「カラー曲線」をほぼ必ずかけてます。あと、ブラーはそこまでかけてません。
            <br><br>
            「ソフトコントラスト」は少し暖かみのある色付けビネット（輪郭部をぼかし背景になじむようするやつ）で四隅がぼやけるように。
            <br><br>
            「明るさとコントラスト」は素材によりますが、ハッキリと人物や建物等が見えやすいように調整してます。
            <br><br>
            「HitFilm Bleach Bypass」もまた映像の明るさ、特に白っぽくしたり暗くしたりするのにほぼ必ずかけてます。
            <br><br>
            「ホワイトグロウ」は画面の白部分が際立つように少しだけかけます
            <br><br>
            「カラー曲線」は全体的に明るい感じ（赤など）を少し出したいときや、かっこいい系やシリアスな感じ（青など）を少し出したいときに使ってます。
            <br><br>
            （青くするほうはこうやったらちょっと美しい感じになるかな、と。あとは色々な映画の影響が強いかも）
            <br><br>
            毎度全体的にこのボカシと明るさ調整等を作品の雰囲気に合わせて調整していくと、わりと簡単に自分の動画っぽい独特な感じになると思います。
            <br><br>
            意識していることは作品ごとに雰囲気といいますか、美しさというか神秘的っぽさ（明るい感じで）を出したいときは白強め。
            <br><br>
            シリアス的だったり、真面目系、夜っぽさなどシックな雰囲気を出したいときは全体的に結構暗めにするようにしてます（一応メインの人物とかがちゃんと見える程度に）
            <br><br>
            あと、色調などを元動画より変えないと個人的になんだか手抜きをしてるように感じちゃうんで、結構やりすぎなくらい弄っちゃってます。
        </td>
    </tr>
</table>
<br>

参考画像

<div class="cocoen">
　　<img src="/madcommentary/HacococoColor_1.png" alt="">
　　<img src="/madcommentary/HacococoColor_2.png" alt="">
</div>

<div class="cocoen">
　　<img src="/madcommentary/HacococoColor_3.png" alt="">
　　<img src="/madcommentary/HacococoColor_4.png" alt="">
</div>

<div class="cocoen">
　　<img src="/madcommentary/HacococoColor_5.png" alt="">
　　<img src="/madcommentary/HacococoColor_6.png" alt="">
</div>

## 背景の四角形のレイアウトを大小するやり方(Disco Necropolis【合作単品】)

<iframe width="560" height="315" src="https://www.youtube.com/embed/ABMEJdI1nvg?start=15" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

年齢制限でここでは流せないですが、0:15~0:27あたりの背景についての質問です。

直接、制作者本人にお聞きしました。

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            この動画の0:15~0:28の背景の四角形のレイアウトを大小するのってどうやってやってるんですか？
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_niggerofpokemon.png" alt="" ></td>
        <td>&nbsp;</td>
        <td valign="top"><img src="/madcommentary/emoji_shizue.webp" alt=""></td>
        <td>&nbsp;</td>
        <td>　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　</td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_leaf_62289.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            拡大率と座標でゴリ押してたなぁ
            <br>
            AviUtlの話になっちゃうけど、中心座標変更アニメ効果使えば超楽かも　　　　　　　　
            <br>
            <a href="https://sosakubiyori.com/aviutl-coord/#:~:text=%E4%B8%AD%E5%BF%83%E4%BD%8D%E7%BD%AE%E3%82%92%E5%A4%89%E6%9B%B4%E3%81%97%E3%81%9F%E3%81%84,%E5%8A%B9%E6%9E%9C%E3%80%8D%E3%82%92%E8%BF%BD%E5%8A%A0%E3%81%97%E3%81%BE%E3%81%99%E3%80%82&text=%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E5%8A%B9%E6%9E%9C%E3%81%AE%E7%A8%AE%E9%A1%9E%E3%82%92,%E4%BD%8D%E7%BD%AE%E3%82%92%E5%A4%89%E6%9B%B4%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82&text=%E3%80%8C%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E7%A7%BB%E5%8B%95%E3%80%8D%E3%81%AB%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF%E3%82%92,%E3%81%99%E3%82%8B%E3%82%88%E3%81%86%E3%81%AB%E3%81%AA%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82">https://sosakubiyori.com/aviutl-coord/</a>
        </td>
    </tr>
</table>

Aeだと、<a href="https://ss-sahara.work/memo/circle-rig/">さはらさんが紹介していたチュートリアル</a>や<a href="https://aescripts.com/flex/">Flex</a>というプラグインを使うと再現が出来そうです。

実際にFlexを使った作例を大好きクラブさんに作ってもらいました。

<video controls width="100%" autoplay loop muted="true" src="/madcommentary/Flex_1.mp4" type="video/mp4" >
 Sorry, your browser doesn't support embedded videos.
</video>

<video controls width="100%" autoplay loop muted="true" src="/madcommentary/Flex_2.mp4" type="video/mp4" >
 Sorry, your browser doesn't support embedded videos.
</video>

## 「4」の単音だけで人力(きゅうくらよん)

<script type="application/javascript" src="https://embed.nicovideo.jp/watch/sm40548351/script?w=640&h=360"></script><noscript><a href="https://www.nicovideo.jp/watch/sm40548351">きゅうくらよん</a></noscript>

## 鳴き声のみで大まかな人力をどのように行っているか(黒白世代宛て図鑑)

<script type="application/javascript" src="https://embed.nicovideo.jp/watch/sm41100374/script?w=640&h=360"></script><noscript><a href="https://www.nicovideo.jp/watch/sm41100374">黒白世代宛て図鑑</a></noscript>

この二つは、似たようなトピックなのでまとめて解説したいと思います。

下の動画は、Vocalizerというエフェクターを使って矩形波を人間の声に近づけた様子です。（音が出ます）

<video controls width="100%" loop="true" src="/madcommentary/Vocalizer_1.mp4" type="video/mp4" >
 Sorry, your browser doesn't support embedded videos.
</video>


<a href="https://www.a-quest.com/products/vocalizer.html">https://www.a-quest.com/products/vocalizer.html</a>

Vocalizerを使うことで人間の声に近いフォルマントを付与することができ、どうぶつやポケモンの鳴き声からも人力VOCALOIDを作ることができます。

日本語の母音は/a/、 /i/、 /u/、 /e/、 /o/の五つだと考えて、五つ分の音声を作り、それを使うことで少ない素材からでも人力VOCALOIDを行うことができるようになります。

男性用の設定と女性用の設定があるので、好みに合わせて設定してください。

また、シンセサイザーの音から同じような方法でUTAU音源を作った例もあります。

<iframe width="312" height="176" src="https://ext.nicovideo.jp/thumb/sm33386516" scrolling="no" style="border:solid 1px #ccc;" frameborder="0"><a href="https://www.nicovideo.jp/watch/sm33386516">【足立レイ】中の人のいない合成音声作った【UTAU音源配布】</a></iframe>

<iframe width="312" height="176" src="https://ext.nicovideo.jp/thumb/sm26933099" scrolling="no" style="border:solid 1px #ccc;" frameborder="0"><a href="https://www.nicovideo.jp/watch/sm26933099">声のようなものを作る【UTAU音源制作過程】</a></iframe>

## 「急転相まって壊したって」のフォントが知りたい(～にょろにょろ合作3～【合作単品】)

<iframe width="560" height="315" src="https://www.youtube.com/embed/-FhtTATPUpU?start=673" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[![img](/madcommentary/NyoroNyoro3_MarshallMaximizer.png)](/madcommentary/NyoroNyoro3_MarshallMaximizer.png)

VDL ペンレター　というフォントです。Adobeに契約するとついてくるフォントの一つです。

<a href="https://fonts.adobe.com/fonts/vdl-penletter">https://fonts.adobe.com/fonts/vdl-penletter</a>

直接、制作者本人と連絡をとることができたのでフォント以外にも参考になるようなことをお聞きしました。

デザインの参考にしたサイトを教えてもらいました。

<a href="https://wkwkdesign.com/japanese-handwritten-font/">https://wkwkdesign.com/japanese-handwritten-font/</a>

他の手書き風のフォントや右肩上がりの加工方法などが書かれています。

また、プロジェクトファイルもこっそり見せてもらいました。

Aeの線プラグインを使って文字が書かれているようなアニメーションをしていました。

<video controls width="100%" autoplay loop muted="true" src="/madcommentary/NyoroNyoro3_MarshallMaximizer_01.mp4" type="video/mp4" >
 Sorry, your browser doesn't support embedded videos.
</video>

このチュートリアルが同じことをしているので参考になると思います。

<iframe width="560" height="315" src="https://www.youtube.com/embed/fFopzxGItEI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 堕ちる堕ちるでいっぱい文字でてくるとこ、最後のトラックメイカーの文字出し(インドア系ならマキシマイザー)

<script type="application/javascript" src="https://embed.nicovideo.jp/watch/sm40494806/script?w=640&h=360&from=64"></script><noscript><a href="https://www.nicovideo.jp/watch/sm40494806?from=64">インドア系ならマキシマイザー</a></noscript>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            堕ちる堕ちるでいっぱい文字でてくるとこ（無数のオブジェクトの配置について）、
            <br>
            最後のトラックメイカーの文字出し（パスのトリミング？）の
            <br>
            使用ソフトや工程、意識していることなどについて教えていただければと思います！
        </td>
    </tr>
</table>

・堕ちる！堕ちる！


[![img](/madcommentary/InDoorMaximizer_1.png)](/madcommentary/InDoorMaximizer_1.png)


<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_c44095762.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            インドア系ならマキシマイザーでは、徹夜の労働で（瞼が）堕ちる！（眠りに）堕ちる！といったストーリーを比喩したかったので、真っ黒なフォントで視界が覆いつくされるような表現を目指しました。<br>
            簡単に作れてお手頃な反面少し動きが単調だと思ったので、カメラで動きを追加しています。<br><br>
        </td>
    </tr>
</table>
            
・トラックメイカー

[![img](/madcommentary/InDoorMaximizer_2.png)](/madcommentary/InDoorMaximizer_2.png)

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_c44095762.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            マーシャル・マキシマイザーの音MADではマーシャル・バトルドーマーのキネポをリスペクトするのがノルマのようになっていたのですが、そのまま再現するのも面白くないなと思い、少しひねってこちらのキネポを採用することになりました。<br>
            KFPマッスグのような角張ったフォントを使うことに意味を持たせるようなキネポを作れたので満足しています。<br><br>
        </td>
    </tr>
</table>

あと、質問とは関係ないですが、この記事が面白かったので紹介します。

<iframe class="note-embed" src="https://note.com/embed/notes/na618e1b379a1" style="border: 0; display: block; max-width: 99%; width: 494px; padding: 0px; margin: 10px 0px; position: static; visibility: visible;" height="400"></iframe><script async src="https://note.com/scripts/embed.js" charset="utf-8"></script>

## 顔面が宇宙人のようになる部分(Big Brother☆.NYD2019【合作単品】)

<script type="application/javascript" src="https://embed.nicovideo.jp/watch/sm36173874/script?w=640&h=360&from=20"></script><noscript><a href="https://www.nicovideo.jp/watch/sm36173874?from=20">Big Brother☆.NYD2019【合作単品】</a></noscript>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            顔面が宇宙人のように変化する部分の、使用ソフトや工程、意識していることなどについて教えてください！
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_hapimashi0131.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            ご質問ありがとうございます<br>
            当該部分は、AfterEffectsで作りました。 <br><br>
            工程については、<br>
            ①：まず、輪郭線で区切った図形と捉えて、それぞれをシェイプレイヤーで再構成しました。<br><br>
            ②：次に、それぞれのシェイプレイヤーの「パス」にキーフレームを打って、パスを変形させることで、顔を変形させるモーフィングアニメにしています。<br><br>
            変形する際は、グラフエディタの速度グラフで、初速と終点の速度を0にして、間で最高速になるように速度に緩急を持たせています。<br><br>
            顔が変形するたびに色味がエキゾチックに変化した方が曲調に合っているかなと思ったので、色味はできるだけビビッドに変化するよう意識しました。<br>
        </td>
    </tr>
</table>

[![img](/madcommentary/NYDBIgBrother_1.png)](/madcommentary/NYDBIgBrother_1.png)

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_hapimashi0131.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            このように、元のキャラの各パーツを塊ごとにシェイプレイヤーでなぞって再構成します。
        </td>
    </tr>
</table>

[![img](/madcommentary/NYDBIgBrother_2.png)](/madcommentary/NYDBIgBrother_2.png)

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_hapimashi0131.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            次に、パスにキーフレームを打って、一つ一つパスを変形させることで違う形を作っていきます。今回は「YUH」を「ばけものYUH」にモーフィングさせてみました。
        </td>
    </tr>
</table>

[![img](/madcommentary/NYDBIgBrother_3.gif)](/madcommentary/NYDBIgBrother_3.gif)

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_hapimashi0131.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            この時点で、このようなアニメーションになります。<br>
            （牙や舌はノーマルYUHにはないので、ノーマル時は他のシェイプの陰に隠すなどして、モーフィングで登場するように調整します。<br>
            ただこの状態では、変形途中のごちゃごちゃした感じが残っていて不格好です。<br>
        </td>
    </tr>
</table>

[![img](/madcommentary/NYDBIgBrother_4.gif)](/madcommentary/NYDBIgBrother_4.gif)

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_hapimashi0131.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            そこで最後に、すべてのパスのキーフレームのグラフの形を変更します。初速を0、途中で最大速になって、止まるときも速度0、とすることで、途中の不格好な部分を隠してにゅっ！とモーフィングできました。
        </td>
    </tr>
</table>

また、記事を見てくれた人への特典としてBB素材もいただきました。

[化け物に変化するYUH姉貴BB.face.mp4](/madcommentary/化け物に変化するYUH姉貴BB.face.mp4)


## 0:58の後ろにある四角形4つが消える箇所，1:01の画面下右側から飛び出した三角形が細かい三角形になり消える箇所(柴又で学ぶ音MAD映像☆)

<script type="application/javascript" src="https://embed.nicovideo.jp/watch/sm37110435/script?w=640&h=360&from=57"></script><noscript><a href="https://www.nicovideo.jp/watch/sm37110435?from=57">柴又で学ぶ音MAD映像☆</a></noscript>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            0:58の後ろにある四角形4つが消える箇所と，1:01の画面下右側から飛び出した三角形が細かい三角形になり消える部分の、使用ソフトや工程、意識していることなどについて教えてください！
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_etsuranyou12345.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            【使用ソフト】<br>
            Aviutl<br>
            <br>
            【工程】<br>
            [1:01] 画面下右側から飛び出した三角形が細かい三角形になり消える箇所<br>
            使用スクリプト：「モザイクマスク(R)」<a href="https://nicovideo.jp/watch/sm28393475">https://nicovideo.jp/watch/sm28393475</a><br>
            　Aviutl上の操作<br>
            ・「図形」の三角形を導入<br>
            ・「アニメーション効果」から「モザイクマスク(R)」を追加<br>
            ・「設定」から「種類」を1（三角形）にして、「ランダムマスク」にチェックを入れ、展開度を0→100にする<br>
            <br>
            [0:58] 後ろにある四角形4つが消える箇所<br>
            使用スクリプト：「粒子化」<a href="https://nicovideo.jp/watch/sm17925979">https://nicovideo.jp/watch/sm17925979</a><br>
            　Aviutl上の操作<br>
            ・「図形」の四角形を導入（カメラ制御下、拡張描画、グロー追加）<br>
            ・「アニメーション効果」から「粒子化」を追加<br>
            ・パラメータを以下の設定にする<br>
            　[進捗率] 0.01→100<br>
            　[泡数] 1000<br>
            　[拡散] 100→200<br>
            ・「設定」は以下のとおり<br>
            　[図形] {"figure","円",0xffffff,25,25}<br>
            　[初期拡大範囲] {50,100}<br>
            　[目標拡大範囲] {-200,-100}<br>
            　[最小描画サイズ] 5.0<br>
            　[透明度範囲] {0,100}<br>
            　[目標透過範囲] {0,100}<br>
            　[移動方向] -90<br>
            　[目標移動範囲] {30,300}<br>
            　[加減速指数] 1.0<br>
            　以下略<br>
            <br>
            なお、図形が地面・水面に反射する表現は以下の動画に作成方法をまとめています。<br>
            「Aviutlでつくる さらざんまいED（実写映像×シェイプモーション）」<a href="https://nicovideo.jp/watch/sm40595866">https://nicovideo.jp/watch/sm40595866</a><br>
            <br>
            【意識していること】<br>
            　今回質問を受けた範囲（モーショングラフィックス）に限定して、制作の際に意識していることを書きます。<br>
            　モーショングラフィックスは、「他の人の映像を大量に見て局所的に丸パクリして再構成する」というのが制作方法になります。音MADはもちろん、映像のプロが制作したMVなども勉強になります。（余談ですが、最近はバーチャルシンガーやボカロのMVが参考になるかと思います。理由は、立ち絵の素材1枚で4分ほどの尺を埋めているものが少なくないため、あの手この手で映像を作っているからです。）
            〈制作において意識していること〉<br>
            　・画面全体に対して図形が占める割合（占有率）を一定以上確保するようにしています。明確な意図が無い限りは余白を埋めた方がベターだと思います。<br>
            　・移動、拡大はイージング（急加速・減速の利いたパラメータ移動）でメリハリをつけた動きにしています。<br>
            　・図形の点滅は最近の流行りとして取り入れていました。<br>
            　・「図形の消滅の仕方」にバリエーションを持たせていました。<br>
            　・Aの場面→Bの場面　と移る場合、Aの最後の動きをBの最初の動きに継承させるとスムーズです。（例：Aの最後で図形がぐんぐん加速する場合、Bの最初で減速（速→遅））。<br>
            　・視線誘導を意識していました。移動、拡大、点滅によって視聴者の目を引き付けて、注目させたいモチーフを目立たせるようにすることがあります。<br>
            <br>
            【アドバイス】<br>
            　・Aviutlのスクリプトをたくさん導入し、自分で色々いじって勉強すると、使える手段が多くなり、様々な発想が浮かびます。<br>
            　・背景をベタ塗りしたフラットモーションが最もとっつきやすいカテゴリかと思います。リアル映像にシェイプモーションを入れると、光の反射を考慮する必要があり、手間が膨大になります。<br><br>
        </td>
    </tr>
</table>

## シャロ、サターニャ、しまりんが映るウィンドウの出し方(Big Brother)

<script type="application/javascript" src="https://embed.nicovideo.jp/watch/sm38312345/script?w=640&h=360"></script><noscript><a href="https://www.nicovideo.jp/watch/sm38312345">Big Brother</a></noscript>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            シャロ、サターニャ、しまりんが映るウィンドウの出し方の、使用ソフトや工程、意識していることなどについて教えてください！
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_mochaml.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            使用ツール:Adobe AfterEffects 2019<br>
            使用プラグイン:なし<br>
            使用エフェクト:Card Wipe<br><br>
            対象の画像をコンポジションに入れる<br>
            コンポジションにCard Wipeをかけ<br>
            ・Rows : 3<br>
            ・Columns : 3<br>
            ・Flip Axis : Random<br>
            ・Flip Order:Top Right to Bottom Left<br>
            ・Timing Randomness : 1.00<br>
            ・Random Seed：複数なら他と被らない数値<br>
            [Camera Position]<br>
            ・X,Y Position : コンポジション中央に画像が来るように（エクスプレッションなら[thisLayer.width/2, thisLayer.height/2]）
            に設定<br><br>
            アニメーション要素<br>
            ・Transition Completion : 50%→0% (リニア)<br>
            [Camera Position]<br>
            ・Y Rotation : -42%→0% (イーズ)<br>
            ・Z Position : 3.2→2.0 (イーズ)<br>
            [Position Jitter]<br>
            ・Z Jitter Amount : 10.0→0 (リニア)<br><br>
            あとは上記のアニメーションに加えてレイヤーのアニメーションでポジションを下から、スケールを0から真ん中へ
            レイヤーコラップスをオンにすれば完成<br>
            シェイプレイヤーもほぼ同じ設定で動作する、レイヤーのアニメーションをシェイプレイヤー側に変更しただけ<br>
        </td>
    </tr>
</table>

## 影莉央さんのキャラクターの良さを引き出すような歌詞改変やセリフ合わせ(影莉央)

<script type="application/javascript" src="https://embed.nicovideo.jp/watch/sm37969246/script?w=640&h=360"></script><noscript><a href="https://www.nicovideo.jp/watch/sm37969246">ルマトアキ【大和亜季誕生祭2020】</a></noscript>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            影莉央さんのキャラクターの良さを引き出すような歌詞改変やセリフ合わせを作るうえで、意識していることや参考にしているものなどについて教えてください！
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_kagerio1.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
        【前提】<br>
        ・心から好きだと思えるキャラクターを選出する<br>
        ・そのキャラクターのファンが傷つくようなネタ・弄り方をしない（例外あり）<br>
        ・一人称などの表記に誤りが無いよう気をつける<br>
        →ここら辺の感覚は一般的な二次創作文化に近いと思います。<br>
        　基本的にはファンが喜んでくれるセリフ・シーン選びを心がけた上で、<br>
        　音MAD的要素（刻み・音程合わせ・リスペクトなど）を加えていくイメージです。<br><br>
        【歌詞改変】<br>
        ・元の歌詞の韻・意味合いをできるだけ活かし、そのキャラクターと合うようなワードを探し当てはめていく。<br>
        　例：ルマトアキ…「感情熱唱→戦場疾走」<br>
        　　　不沈艦前夜…「始まりの景色を見惚れては→シンガリの景色を見惚れては」<br>
        ◎キャラクターと合うワードの探し方<br>
        　そのキャラのwikiなどを参考に特徴的なワードを書き出し、類語辞典などを使用してレパートリーを増やす。<br>
        　「韻ノート」というサイトに原曲の歌詞を打ち込んで探すのもアリです。<br>
        　<a href="https://in-note.com">https://in-note.com</a><br><br>
        【セリフ合わせ】<br>
        ・極力セリフ元々の魅力を潰さないようなセリフ合わせを行う<br>
        例：テロップ無しでも元のセリフが聞き取れるようにする（子音を削りすぎない）<br>
        　　元のセリフのテンポ感を残す…促音・間などを残す<br>
        ・原曲のキメとなるパート（サビ前など）に、そのキャラの魅力が全面に出ているセリフを持ってくる<br>
        例：じゃじゃうまーっ！！！ラスサビ前→アンタの人生面白くなっただろ？<br>
        ・その原曲を選んだ理由(根拠)が伝わるようなセリフを選ぶ<br>
        　→俗に言う原曲要素回収です。キャベツさんの音MADなどが特に参考になると思います。<br><br>
        【参考にしているもの】<br>
        ・韻踏みに特化した楽曲（Creepy Nutsなど）<br>
        ・この世の音MAD全て<br>
        </td>
    </tr>
</table>

## きれいに白黒にする方法(？/葉月味)

<iframe width="560" height="315" src="https://www.youtube.com/embed/LukOAsEtEmY?start=18" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            0:20~0:39について、きれいな二値化をするための使用ソフトや工程、意識していることなどについて教えてください！
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_hadkimi_.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            了解です！近日中に文章にまとめて送ります　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
        </td>
    </tr>
</table>

![Alt text](/madcommentary/2000yearslater.png)

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            <img src="/madcommentary/linestamp.png" alt="">　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_hadkimi_.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            pf無くしててワロタなんだけど　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　<br>
            どうしようかなあ
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_sehatakuro.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            なにか特殊な方法で二値化してたんですか？　　　　　　　　　　　　　　　　　　　　　　　　　
        </td>
    </tr>
</table>

<table>
    <tr>
        <td valign="top"><img src="/madcommentary/icon_hadkimi_.png" alt=""></td>
        <td>&nbsp;</td>
        <td>
            AviUtlの2値化（ティム）を使っただけだとは思う<br>
            あと電子書籍から漫画コマを取り込むときにちょっと2値化しやすいようにキレイにしたりコントラストなど調整した覚えがある
        </td>
    </tr>
</table>

## おわりに

今回、さまざまな作品についてインタビューをしたり細かく分析したりしてみて気づいたことは、よい作品や技術的にすぐれている作品というものは地道な努力や調整の上で成り立っているものだということです。

ぱっと見どう作ってるのかわからない物も細かく分解したり制作手法を聞くと、実際は自分と使っているツールや作り方と同じだったりしました。

制作手法もプラグインも調べれば、誰かがブログやnoteで書いていたりします。もしくは誰かに聞けば、教えてくれるかもしれません。

つまり、ノウハウやツールの情報はすでに出尽くし、蓄積されていて、あとはどれだけ熱量をもって取り組めるかということが、作品の質を大きく左右するのではないでしょうか！

最後に、個人的に参考になっている音MAD作者の記事をいくつか紹介して終わろうと思います

- [20221109:切り貼り人力をしたい/不可逆褐色](https://note.com/eroerojpeg/n/nc0e8bcf0f4b9)
- [20221106:ffmpegの導入とパスの通し方/[まいまい]](https://ytpmv.info/?p=1491)
- [20201215:初期に知っときたかったAviUtlの使い方/芋タルト](https://immortalt.hatenablog.com/entry/2020/12/15/202001)
- [20201107:色んな「効果線」をAviUtlで作る/芋タルト](https://immortalt.hatenablog.com/entry/2020/11/07/211822)
- [20200608:色から見る音MAD/芋タルト](https://immortalt.hatenablog.com/entry/2020/06/08/210632)
- [20200107:【REAPER】MIDIから音声オブジェクトを自動生成するスクリプト【midi2item】/[まいまい]](https://ytpmv.info/ReaScript-midi2item/)
- [20191231:個人的　音MADの作り方/芋タルト](https://immortalt.hatenablog.com/entry/ar1845344)
- [FLAPPER](https://seguimiii.com/)

Aviutlの使い方や流行りの映像表現をAviutlで作るチュートリアルなど

- [【5,000記事以上】ニコニコメドレー/音MAD/その他周辺のブロマガのうち収集できたものを公開します](http://medley26kvocaloid.blog.fc2.com/blog-entry-75.html)

26Kさんがアーカイブしている音MAD関連のブロマガです。

GoogleDriveでアーカイブしたサイトを見ることができます。

<https://drive.google.com/drive/folders/1RRyWgtUa_yHy-itqxCfPqbCODZt6m1eW>

少々さんのVSTやAviutlについての記事がおすすめです。

今回の記事を書くにあたって、たくさんの人にご協力いただきました。質問を送っていただいた方、質問に回答していただいた方、技術共有記事を書いている方、本当にありがとうございます。また、この記事を作るアイデアのきっかけになったちょのゆしさんにもお礼を申し上げます。

この記事を最後まで呼んでくれた人の中から、良い作品が生まれることを願っています！

↓↓↓↓この記事がよかったらツイッターで共有してください！

<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false">Tweet</a>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
