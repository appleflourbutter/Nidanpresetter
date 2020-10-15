# NidanPresetterとは  
(English below)
NidanPresetterは2段プリセットの照明卓をsACNで実現するためのソフトウェアです。  
2つのユニバースの信号を受け、クロスフェーダーの位置に従って処理をし、1つのユニバースで出力します。クロスフェーダーもsACN上で操作します。  
クロスフェーダーを動かすことで、2段プリセットの卓のようなフェードをすることができます。

# NidanPresetterでできる（ようになるはずの）こと  
2台の卓を用意し、違うユニバースで同じパッチをします。また、どちらかの卓で3つ目のユニバースにクロスフェーダーとなるフェーダーをパッチします。2台の卓とNidanPresetterの  
実際には複数のユニバースにsACNでパッチできる卓であれば1台でも十分なはずです。  

# これから対応したいこと  
- ムービングライトなどのフェードしてほしくないパラメーター（ゴボやカラーホイール）をカットチェンジできるように  
- クロスフェードの処理方法を従来の卓と同じように  
- GUIで使いやすく  
- Windows対応  
- コードの書き直し  

# NidanPresetter is...  
NidanPresetter is a software which enables 2 scene crossfade using sACN. The word "Nidan" means 2 scenes in Japanese.  
It recieves 2 universes and process these according to the position of crossfader. Crossfader is also one channel on sACN universe.  

