CF='https://d8j0ntlcm91z4.cloudfront.net/user_3GPAF0rrhhkySItNy2PPzIih3Bo/hf_20261121_'
GH='https://raw.githubusercontent.com/sardov/abcref/main/content/'
V={ # key: (title, still, video)
'R1':('wasted',CF+'170206_8a33a85c-2efa-4a32-b7a6-74426563f075.png',CF+'170543_b31612e0-85b6-4553-aaed-48a6fd7de84d.mp4'),
'R2':('★★★★★',CF+'170206_c56c7c07-cc8b-4e72-9d7f-25a5a63ef169.png',CF+'170328_e8b0cf91-f09a-479a-b705-2daeaf2345aa.mp4'),
'R3':('worth the wait',CF+'170206_9c765d77-ba46-4b52-9d92-3066c336718c.png',CF+'170327_6fc6454a-37a7-4a87-8c6a-16fb21e41346.mp4'),
'N0':('rush b',CF+'172323_8caf6847-9510-454a-88de-a4116a2ac31d.png',CF+'172436_fddee40e-e227-40f8-a86a-71c571533d32.mp4'),
'N1':('1 hp',CF+'172321_9df1751b-826a-45aa-b5b3-4887483b3bc2.png',CF+'172437_eb467f92-3289-4b32-818a-ea6949c591b9.mp4'),
'N2':('clutch',CF+'172321_2bdf3f90-088a-46b8-ab00-131d4f972637.png',CF+'172615_fca9164d-ff95-40dc-898d-e1c2ae33ec48.mp4'),
'N3':('ff 15',CF+'172322_3ff78624-af78-4bd0-b9c1-9c8ff400894b.png',CF+'172615_a61edf1e-8e01-4bcf-b255-4d46bab5db8a.mp4'),
'N4':('mid or feed',CF+'172427_35109786-46af-4564-a8db-58415e82b1d6.png',CF+'172751_45690f70-41ba-4b7d-9578-c239f5ce1d54.mp4'),
'N5':('afk',CF+'172427_bded3b71-4354-4e65-b232-77f6bc2db424.png',CF+'172749_2595cbc7-2d77-40c6-9803-e1601c6aec05.mp4'),
'N6':('touch grass',CF+'172427_27faf646-578c-4dd4-bfd4-23fcbf691b9d.png',CF+'172930_dc45fbc6-cf5d-47e7-8f9f-c6be4bbe297b.mp4'),
'N7':('respawning',CF+'172428_3c1370bb-70dd-44c4-8f3d-04eae8cc8cd2.png',CF+'172930_94a74d41-5001-4b64-aad7-8978008d5a2a.mp4'),
'N8':('gg, go next — макро',CF+'172514_e182c16d-d841-4cf2-8c2d-34a811ea94d9.png',CF+'173056_9f7bcd7e-9d00-41a0-ab4e-f5bce8afd91c.mp4'),
'N9':('she will appreciate this',CF+'172612_f4174475-5765-40d0-b05f-e53214751854.png',CF+'173209_f83e6163-4358-4037-aa37-f73a8f4f021d.mp4'),
'N10':('florida man',CF+'172613_59cc9ed0-55e9-4568-aca0-ddc1498d536e.png',CF+'173209_8be4139f-eec6-4942-91e7-de4902022ed6.mp4'),
'V1':('gg, go next — футболка на камне (15 с, премиум)',CF+'144950_4307cf32-e4a5-45ba-9da4-a0cda709b119.png',CF+'145048_3b014acb-ae04-443f-9a34-bb9bd5b199b7.mp4'),
'V2':('UGC — ИИ-человек показывает вышивку (15 с)',None,CF+'145146_474f9a69-041b-47a0-a559-d8de84e11a86.mp4'),
}
GTA=[GH+'gta-refs/c_hook.jpg']+[CF+x for x in ['170024_a3f3a10b-34d9-484d-8ab4-4abea1b2d465.png','170302_e2ff6247-5b78-4fb7-a97e-daa1c1f62cc4.png','170024_08c0fc28-ab7a-448a-9480-1d1e0c4d4b38.png','170024_26fda8ef-e6c1-4874-9d40-d4b792d5a367.png','170114_f8e36539-d887-4848-b1b5-abdb680ed306.png','170116_9bb35127-174c-410e-a686-e83ddee5a289.png','170114_0fad472f-39c3-4d1f-bbfd-f6c0de124e24.png']]+[GH+'gta-refs/c_end.jpg']
def car(k): return [GH+f'plan-week1/{k}_{i:02d}.jpg' for i in range(1,10)]
ST={'new':GH+'plan-week1/st_newpost.jpg','poll':GH+'plan-week1/st_poll.jpg','q1':GH+'plan-week1/st_q1.jpg','q2':GH+'plan-week1/st_q2.jpg','s1':GH+'test-2026-11-21/F01.jpg','s2':GH+'test-2026-11-21/F02.jpg'}
def cols(urls,n=5):
    out=[]
    for i in range(0,len(urls),n):
        chunk=urls[i:i+n]; s='<columns>\n'
        for j,u in enumerate(chunk): s+=f'<column>\n![{i+j+1}]({u})\n</column>\n'
        for _ in range(n-len(chunk)): s+='<column>\n</column>\n'
        out.append(s+'</columns>')
    return '\n\n'.join(out)
def post(time,kind,urls,cap,n=5): return f'### 📸 Instagram · {time} · {kind}\n\n{cols(urls,n)}\n\n<b>Подпись:</b> {cap}\n\n<b>Оценка:</b> —'
def vid(time,k,cap,note=''):
    t,s,v=V[k]; img=f'<columns>\n<column>\n![первый кадр]({s})\n</column>\n<column>\n</column>\n<column>\n</column>\n</columns>\n\n' if s else ''
    return f'### 🎬 TikTok + Shorts + Reels · {time} · «{t}»\n\n{img}▶️ [смотреть видео]({v})\n\n<b>Подпись:</b> {cap}{note}\n\n<b>Оценка:</b> —'
def sto(items): 
    s='### 📱 Сторис Instagram · '+' · '.join(t for t,_ in items)+'\n\n<columns>\n'
    for _,u in items: s+=f'<column>\n![сторис]({u})\n</column>\n'
    for _ in range(4-len(items)): s+='<column>\n</column>\n'
    return s+'</columns>'
D=[]
D.append(('Вс 22 нояб',[vid('11:00 ET (18:00 Кипр)','R1','wasted. you heard it a thousand times. #gta6 #gaming #gamer'),
 post('12:00 ET (19:00 Кипр)','карусель 9 слайдов, стиль D — GTA',GTA,"you heard it a thousand times. now wear it. which one would you wear? comment the number. what's missing? drop the phrase you'd wear. #gta6 #gaming #minimalstyle"),
 vid('19:00 ET (02:00 Кипр, Пн)','R2','★★★★★. you know the feeling. #gta6 #gaming'),
 sto([('12:30 ET «new post»',ST['new']),('20:00 ET «which one?»',ST['poll'])])]))
D.append(('Пн 23 нояб',[post('08:00 ET (15:00 Кипр)','одно фото — на человеке без лица',[CF+'144804_dee3cf59-aa87-4103-9d60-b1e0da2c7d9d.png'],'gg, go next. what you say when it\'s over. #gaming #cs2 #leagueoflegends',3),
 vid('13:00 ET (20:00 Кипр)','N0','rush b. a plan, technically. #cs2 #counterstrike #gaming'),
 vid('21:00 ET (04:00 Кипр, Вт)','N9','she will appreciate this. #gta6 #gaming'),
 sto([('09:00 ET «no logos»',ST['q1']),('18:00 ET «join the lobby»',ST['s2'])])]))
D.append(('Вт 24 нояб',[vid('07:00 ET (14:00 Кипр)','N1','1 hp. still in it. #cs2 #clutch #gaming'),
 vid('16:00 ET (23:00 Кипр)','V1','no logos. just signals. #gaming #minimalism'),
 post('18:00 ET (01:00 Кипр, Ср)','карусель 9 слайдов, стиль A — CS',car('cs'),'only players will understand. which one would you wear? comment the number. #cs2 #counterstrike #gaming'),
 sto([('10:00 ET «you see it»',ST['q2']),('18:30 ET «new post»',ST['new'])])]))
D.append(('Ср 25 нояб',[vid('10:00 ET (17:00 Кипр)','N3','ff 15. a polite way to give up. #leagueoflegends #lol #gaming'),
 post('12:00 ET (19:00 Кипр)','текстовый пост',[GH+'test-2026-11-21/C01.jpg'],'clothing for those who know. #gaming',3),
 vid('20:00 ET (03:00 Кипр, Чт)','N10','florida man. #gta6 #gaming'),
 sto([('12:30 ET «collection 01»',ST['s1']),('21:00 ET «which one?»',ST['poll'])])]))
D.append(('Чт 26 нояб — День благодарения в США',[vid('09:00 ET (16:00 Кипр)','N5','afk. happy thanksgiving. back in 5. #gaming #thanksgiving'),
 post('14:00 ET (21:00 Кипр)','карусель 9 слайдов, стиль C — LoL / Dota',car('lol'),'if you get it, you get it. pick one. comment it. #leagueoflegends #dota2 #gaming'),
 vid('18:00 ET (01:00 Кипр, Пт)','N4','mid or feed. a negotiation. #leagueoflegends #gaming'),
 sto([('14:30 ET «new post»',ST['new']),('20:00 ET «no logos»',ST['q1'])])]))
D.append(('Пт 27 нояб — Black Friday',[post('10:00 ET (17:00 Кипр)','одно фото — экспонат на постаменте',[CF+'144950_4307cf32-e4a5-45ba-9da4-a0cda709b119.png'],'no sale. no countdown. just signals. join the lobby — link in bio. #blackfriday #gaming',3),
 vid('12:00 ET (19:00 Кипр)','V2','what you say at the end of every round. #gaming',' <b>⚠️ включить метку «ИИ-контент» в TikTok/Reels/Shorts.</b>'),
 vid('21:00 ET (04:00 Кипр, Сб)','N2',"clutch. 1v3. don't talk to me. #cs2 #gaming"),
 sto([('10:30 ET «join the lobby»',ST['s2']),('19:00 ET «you see it»',ST['q2'])])]))
D.append(('Сб 28 нояб',[vid('10:00 ET (17:00 Кипр)','N6','touch grass. tomorrow. #gaming #weekend'),
 post('11:00 ET (18:00 Кипр)','карусель 9 слайдов, стиль B — общее',car('gen'),'you said it a thousand times. now wear it. tag the one who says this. #gaming #gamer'),
 vid('17:00 ET (00:00 Кипр, Вс)','R3','worth the wait. #gta6 #retrogaming'),
 sto([('11:30 ET «new post»',ST['new']),('20:00 ET «which one?»',ST['poll'])])]))
D.append(('Вс 29 нояб',[vid('12:00 ET (19:00 Кипр)','N7','respawning. give me a second. #gaming'),
 post('19:00 ET (02:00 Кипр, Пн)','музейная этикетка',[GH+'test-2026-11-21/D01.jpg'],'said at the end of every round. worn long after. #gaming #minimal',3),
 vid('20:00 ET (03:00 Кипр, Пн)','N8','gg, go next. stitched, not printed. #gaming #embroidery'),
 sto([('13:00 ET «collection 01»',ST['s1']),('21:00 ET «no logos»',ST['q1'])])]))
head='''<callout icon="👉" color="yellow_bg">
<b>Статус: ждёт утверждения Jakov.</b> Ничего не опубликовано и не запланировано. Под каждым пунктом — «Оценка»: пиши в чат «день + что + гуд/не гуд», я переношу. После «ок» — ставлю всё в расписание Metricool.
</callout>

<b>Период:</b> вс 22 – вс 29 ноября (8 дней). <b>Время</b> — по Нью-Йорку (ET, аудитория США) и в скобках по Кипру; время специально разное, чтобы найти лучшее.

<b>В неделю:</b> 8 постов в ленту Instagram (4 карусели в 4 разных стилях, 2 фото, 1 текстовый, 1 этикетка) · 16 сторис (2 в день) · 16 роликов по 2 в день — каждый ролик идёт сразу в TikTok, YouTube Shorts и Instagram Reels (Reels — без показа в сетке профиля).

<b>Ролики:</b> 14 «фото + оживление» по 5 с (Kling 4.0 Flash) + V1 «футболка на камне» 15 с + V2 UGC 15 с (с меткой ИИ). Видео открываются по ссылке «смотреть видео» (Notion не берёт файлы больше 5 МБ).

<b>Потрачено на пачку:</b> ≈ 155 кр. (GTA-пачка 44.5 + неделя 110.5). Карусели CS / LoL / общее, текстовые посты, этикетка и сторис — шаблоны Claude, бесплатно.

<b>Ещё нужно до публикации:</b> 1) TikTok перевести в Business-аккаунт — для трендовой музыки к роликам; 2) звук к роликам — подберу трендовый перед постингом; 3) Metricool Starter (бесплатных 20 постов в месяц на такой объём не хватит).

## Сводка

| День | Пост в ленту | Ролики | Сторис |
| --- | --- | --- | --- |
| Вс 22 | карусель GTA (стиль D) | wasted · ★★★★★ | 2 |
| Пн 23 | фото на человеке | rush b · she will appreciate this | 2 |
| Вт 24 | карусель CS (стиль A) | 1 hp · V1 на камне | 2 |
| Ср 25 | текстовый «no logos» | ff 15 · florida man | 2 |
| Чт 26 | карусель LoL / Dota (стиль C) | afk · mid or feed | 2 |
| Пт 27 | фото «экспонат» (Black Friday без скидок) | UGC (метка ИИ) · clutch | 2 |
| Сб 28 | карусель «общее» (стиль B) | touch grass · worth the wait | 2 |
| Вс 29 | музейная этикетка | respawning · gg, go next макро | 2 |
'''
body=head+'\n\n'+'\n\n---\n\n'.join(f'## {d}\n\n'+'\n\n'.join(items) for d,items in D)
open('plan/plan.md','w').write(body); print(len(body))
