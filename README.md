# jacktor-foto-classifier
Pyhton script that recursively scans a folder for fotos, classifies the images with MobileNetSSD and writes the results to a sqlite database.

```
jacktor-foto-classifier.py [-h] -p C:\Users\frank\Pictures
```

## Example usage for scanning all pictures within C:\Users\frank\Pictures:
```
       __       ___       ______  __  ___ .___________.  ______   .______
      |  |     /   \     /      ||  |/  / |           | /  __  \  |   _  \
      |  |    /  ^  \   |  ,----'|  '  /  `---|  |----`|  |  |  | |  |_)  |
.--.  |  |   /  /_\  \  |  |     |    <       |  |     |  |  |  | |      /
|  `--'  |  /  _____  \ |  `----.|  .  \      |  |     |  `--'  | |  |\  \----.
 \______/  /__/     \__\ \______||__|\__\     |__|      \______/  | _| `._____|

[create table start]: picture
[create table end]: picture
[create table start]: tag
[create table end]: tag
[create index filepath_index start]
[create index filepath_index end]
[create index tag_index start]
[create index tag_index end]
[NEW]: C:\Users\frank\Pictures\001.png
[resize start]: C:\Users\frank\Pictures\001.png
[resize end]: C:\Users\frank\Pictures\001.png
[tag]: chair 0.338716000319 (0.013702359050512314, 0.13602593541145325, 0.27015822849193205, 0.40976005264475374)
[NEW]: C:\Users\frank\Pictures\002.png
[resize start]: C:\Users\frank\Pictures\002.png
[resize end]: C:\Users\frank\Pictures\002.png
[tag]: car 0.349595636129 (0.013234034180641174, 0.35538554191589355, 0.2454553307695563, 0.5654960744994603)
[NEW]: C:\Users\frank\Pictures\003.png
[resize start]: C:\Users\frank\Pictures\003.png
[resize end]: C:\Users\frank\Pictures\003.png
[tag]: car 0.336040169001 (0.010434821248054504, 0.3909158706665039, 0.23896551668727783, 0.5656052574662049)
[NEW]: C:\Users\frank\Pictures\004.png
[resize start]: C:\Users\frank\Pictures\004.png
[resize end]: C:\Users\frank\Pictures\004.png
[tag]: car 0.300976276398 (0.016742900013923645, 0.3565738797187805, 0.24600800247299687, 0.5630271847238018)
[NEW]: C:\Users\frank\Pictures\005.png
[resize start]: C:\Users\frank\Pictures\005.png
[resize end]: C:\Users\frank\Pictures\005.png
[tag]: car 0.275115162134 (0.015696018934249878, 0.3587551414966583, 0.2461565194753655, 0.5639518866559121)
[NEW]: C:\Users\frank\Pictures\006.png
[resize start]: C:\Users\frank\Pictures\006.png
[resize end]: C:\Users\frank\Pictures\006.png
[tag]: car 0.41229724884 (0.017718106508255005, 0.35149040818214417, 0.24476430251796202, 0.5657870725908024)
[tag]: pottedplant 0.39839759469 (0.2750452756881714, 0.6780396699905396, 0.002734956191394232, 0.33920364540840503)
[NEW]: C:\Users\frank\Pictures\007.png
[resize start]: C:\Users\frank\Pictures\007.png
[resize end]: C:\Users\frank\Pictures\007.png
[tag]: car 0.250188827515 (0.014773279428482056, 0.384657621383667, 0.23756285424641585, 0.5689112613640421)
[NEW]: C:\Users\frank\Pictures\008.png
[resize start]: C:\Users\frank\Pictures\008.png
[resize end]: C:\Users\frank\Pictures\008.png
[NEW]: C:\Users\frank\Pictures\009.png
[resize start]: C:\Users\frank\Pictures\009.png
[resize end]: C:\Users\frank\Pictures\009.png
[tag]: chair 0.250518172979 (0.013137970119714737, 0.1347956657409668, 0.2700209785279007, 0.410751518485583)
[NEW]: C:\Users\frank\Pictures\010.png
[resize start]: C:\Users\frank\Pictures\010.png
[resize end]: C:\Users\frank\Pictures\010.png
[tag]: car 0.262513965368 (0.015832364559173584, 0.3511033058166504, 0.24449458102133706, 0.5651823411343302)
[NEW]: C:\Users\frank\Pictures\011.png
[resize start]: C:\Users\frank\Pictures\011.png
[resize end]: C:\Users\frank\Pictures\011.png
[tag]: car 0.263093054295 (0.010599106550216675, 0.9554851055145264, -0.0025414213349547565, 0.5620273356699239)
[NEW]: C:\Users\frank\Pictures\012.png
[resize start]: C:\Users\frank\Pictures\012.png
[resize end]: C:\Users\frank\Pictures\012.png
[tag]: car 0.350062340498 (0.012924447655677795, 0.3908414840698242, 0.23748363288310678, 0.5658312688899946)
[NEW]: C:\Users\frank\Pictures\013.png
[resize start]: C:\Users\frank\Pictures\013.png
[resize end]: C:\Users\frank\Pictures\013.png
[tag]: car 0.307122707367 (0.015263080596923828, 0.397235244512558, 0.23878103570093082, 0.5655558300420704)
[NEW]: C:\Users\frank\Pictures\014.png
[resize start]: C:\Users\frank\Pictures\014.png
[resize end]: C:\Users\frank\Pictures\014.png
[tag]: chair 0.278988718987 (0.013561494648456573, 0.13574370741844177, 0.2704335332084473, 0.40984361651242196)
[NEW]: C:\Users\frank\Pictures\015.png
[resize start]: C:\Users\frank\Pictures\015.png
[resize end]: C:\Users\frank\Pictures\015.png
[tag]: car 0.282574802637 (0.0143585205078125, 0.39503318071365356, 0.23883279365829274, 0.5655459713835254)
[tag]: chair 0.281371086836 (0.013181760907173157, 0.13569234311580658, 0.27067810506592654, 0.4094918568929036)
[NEW]: C:\Users\frank\Pictures\016.png
[resize start]: C:\Users\frank\Pictures\016.png
[resize end]: C:\Users\frank\Pictures\016.png
[tag]: car 0.314916551113 (0.01841883361339569, 0.3465741276741028, 0.2455072060919009, 0.564406256803145)
[tag]: chair 0.262014627457 (0.13246917724609375, 0.2963867783546448, 0.2506724222132258, 0.4199327128178292)
[tag]: chair 0.251986920834 (0.013274706900119781, 0.13597732782363892, 0.2707295947604709, 0.4098099830616711)
[NEW]: C:\Users\frank\Pictures\017.png
[resize start]: C:\Users\frank\Pictures\017.png
[resize end]: C:\Users\frank\Pictures\017.png
[tag]: chair 0.288315206766 (0.013764355331659317, 0.1365792453289032, 0.2697703372241743, 0.41081821532859747)
[tag]: pottedplant 0.393738031387 (0.27521011233329773, 0.6804835796356201, 0.005432825048261554, 0.3300761707053741)
[NEW]: C:\Users\frank\Pictures\018.png
[resize start]: C:\Users\frank\Pictures\018.png
[resize end]: C:\Users\frank\Pictures\018.png
[tag]: chair 0.338716000319 (0.013702359050512314, 0.13602593541145325, 0.27015822849193205, 0.40976005264475374)
[NEW]: C:\Users\frank\Pictures\019.png
[resize start]: C:\Users\frank\Pictures\019.png
[resize end]: C:\Users\frank\Pictures\019.png
[tag]: chair 0.338716000319 (0.013702359050512314, 0.13602593541145325, 0.27015822849193205, 0.40976005264475374)
[NEW]: C:\Users\frank\Pictures\320849.jpg
[resize start]: C:\Users\frank\Pictures\320849.jpg
[resize end]: C:\Users\frank\Pictures\320849.jpg
[NEW]: C:\Users\frank\Pictures\320863.jpg
[resize start]: C:\Users\frank\Pictures\320863.jpg
[resize end]: C:\Users\frank\Pictures\320863.jpg
[tag]: bird 0.903577387333 (-0.005240589380264282, 0.9999567270278931, 0.013560488351348899, 0.45161177489386045)
libpng warning: iCCP: known incorrect sRGB profile
[NEW]: C:\Users\frank\Pictures\d204ad15f31db498 (1).png
[resize start]: C:\Users\frank\Pictures\d204ad15f31db498 (1).png
[resize end]: C:\Users\frank\Pictures\d204ad15f31db498 (1).png
libpng warning: iCCP: known incorrect sRGB profile
[NEW]: C:\Users\frank\Pictures\d204ad15f31db498.png
[resize start]: C:\Users\frank\Pictures\d204ad15f31db498.png
[resize end]: C:\Users\frank\Pictures\d204ad15f31db498.png
[NEW]: C:\Users\frank\Pictures\DiscoDingo_SylviaRitter.jpg
[resize start]: C:\Users\frank\Pictures\DiscoDingo_SylviaRitter.jpg
[resize end]: C:\Users\frank\Pictures\DiscoDingo_SylviaRitter.jpg
[NEW]: C:\Users\frank\Pictures\heart-clip-artinprogress-md.png
[resize start]: C:\Users\frank\Pictures\heart-clip-artinprogress-md.png
[resize end]: C:\Users\frank\Pictures\heart-clip-artinprogress-md.png
[NEW]: C:\Users\frank\Pictures\Camera Roll\WIN_20190319_17_58_05_Pro.jpg
[resize start]: C:\Users\frank\Pictures\Camera Roll\WIN_20190319_17_58_05_Pro.jpg
[resize end]: C:\Users\frank\Pictures\Camera Roll\WIN_20190319_17_58_05_Pro.jpg
[tag]: person 0.977006971836 (0.35575246810913086, 0.7008928060531616, 0.14559984542481844, 0.5624866351464294)
[NEW]: C:\Users\frank\Pictures\Camera Roll\WIN_20190319_17_58_33_Pro.jpg
[resize start]: C:\Users\frank\Pictures\Camera Roll\WIN_20190319_17_58_33_Pro.jpg
[resize end]: C:\Users\frank\Pictures\Camera Roll\WIN_20190319_17_58_33_Pro.jpg
[tag]: person 0.95952129364 (0.371345579624176, 0.88576740026474, 0.16081494118090922, 0.5585347549824775)
[NEW]: C:\Users\frank\Pictures\Camera Roll\WIN_20190319_17_58_42_Pro.jpg
[resize start]: C:\Users\frank\Pictures\Camera Roll\WIN_20190319_17_58_42_Pro.jpg
[resize end]: C:\Users\frank\Pictures\Camera Roll\WIN_20190319_17_58_42_Pro.jpg
[tag]: person 0.994366168976 (0.3745580315589905, 0.7374613881111145, 0.1598877410513104, 0.5612298238461866)
```

## Possible classified objects
```
["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
```

## Result database C:\Users\frank\Pictures\photos.sqlite
- Table picture: id, filepath (ID of the picture, filepath of the picture)
- Table tags: id, picture_id, tag, confidence, x_start, x_end, y_start, y_end (ID of the tag, tag = e.g.: car, person..., confidence = probability that this tag is correct; value is between 0...1,  x_start relative x-start coordinate of the detected bounding box, x_end...)

![pictures table](https://i.imgur.com/zmjggA6.png "Pictures table")
![tags table](https://i.imgur.com/NHEjOlc.png "Tags table")
