import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptik')
@bot.command()
async def merhaba(ctx):
    await ctx.send("Merhaba Hoşgeldin ben çevredostu sunucusunun botuyum.Ben  sana iklim değişikliği hakkında bilgi vermek için buradayım. İklım değışıklığı ıle ılgılı vıdeolar ızlemek ıçın vıdeolar yazabılırsın soru sormak ıçın sorular yazabılırsın. " )

@bot.command()
async def videolar(ctx):
    await ctx.send("iklim değişikliği ile ilgili video görmek istiyorsan 'video1' eğer iklim değişikliğinin sonucunda neler olucağı hakkında bir video görmek istersen 'video2',eğer iklim değişikliği ile ilgili farkındalık videosu görmek istiyorsan 'video3' yazabilirsin.")

@bot.command()
async def video1(ctx):
    await ctx.send("https://www.youtube.com/watch?v=ZeMd4ii76VQ&pp=ygUlaWtsaW0gZGXEn2nFn2lrbGnEn2kgaWxlIGlsZ2lsaSB2aWRlbw%3D%3D")

@bot.command()
async def video2(ctx):
    await ctx.send("https://www.youtube.com/watch?v=HStCv8ixyWg&pp=ygUlaWtsaW0gZGXEn2nFn2lrbGnEn2kgaWxlIGlsZ2lsaSB2aWRlbw%3D%3D")

@bot.command()
async def video3(ctx):
    await ctx.send("https://www.youtube.com/watch?v=yBIGbXS08qs&pp=ygUlaWtsaW0gZGXEn2nFn2lrbGnEn2kgaWxlIGlsZ2lsaSB2aWRlbw%3D%3D")

@bot.command()
async def sorular(ctx, count_heh = 5):
    await ctx.send( "İklim değişikliğinin tek sorumlusu insanlar mı?\n"
                   "soru2:İklim değişikliği? Küresel ısınma? İklim krizi? Hangisi doğru?\n"
                   "soru3:İklim değişikliği hayvanlara nasıl etki ediyor?\n"
                   "soru4:İklim değişikliği insanları nasıl etkiliyor?\n"
                   "soru5:İklim değişikliği okyanusları nasıl etkiliyor?\n"
                   "soru6:İklim değişikliğinde ormansızlaşmanın payı var mı?\n"
                   "soru7:Küresel ısınma dünyayı tehdit mi ediyor?\n"
                   "soru8:Yaşananlar küresel iklim değişikliği mi?\n"
                   "soru9:Dünya su tehdidi ile mi karşı karşıya?\n"
                   "soru10:Son yaşanan sel olayının sebebi aşırı yağışlar mı?\n"
                   "soru11:Kuraklığı güçlü şekilde hissedecek miyiz?\n"
                   "soru12:BM'nin 'Dünya Su Gelişim Raporuna' dair ne diyorsunuz?\n"
                   "soru13:Su ihtiyacı sebebiyle göçler artacak mı?\n"
                   "soru14:İklim değişikliğine karşı nasıl bir politika izlenmeli?\n"
                   "soru15:İklim değişikliğinin gerçekten olduğunu nasıl bilebiliriz?\n")

@bot.command()
async def soru1(ctx, count_heh = 5):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\iklim-degisikligi-ve-korunan-alanlar-20170923153600.jpg"
    await ctx.send("Bilim insanlarının yüzde 97’si bu sorunun yanıtında hemfikir: Evet atmosferde yaşanan sıcaklık artışına insan faaliyetleri neden oluyor. Fosil yakıtların ölçüsüzce kullanımı, ormansızlaşma, çevre kirliliğinin suya, toprağa ve havaya verdiği zarar, atmosferdeki sera gazlarının hızla artmasına ve küresel ısınmaya yol açıyor." * count_heh, file=discord.File(image))

@bot.command()
async def soru2(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\iklim-degisikligi (1).jpg"
    await ctx.send("Sürdürülebilirlik gündeminde her gün karşımıza çıkan bu üç kavramın atıfta bulunduğu tek gerçek var: Dünya atmosferinin ortalama sıcaklığı günden güne hızla artıyor. Artan sıcaklıklar iklimsel özellikleri değiştiriyor. Değişen iklimsel özellikler ise aşırı hava olaylarına yani krize yol açıyor. Eğer sıcaklık artışları kontrol altına alınmazsa ekosistemler zarar görecek, su krizi oluşacak, okyanuslar hatta toprak bile etkilenecek. Tüm bu olasılıklar sürdürülebilir yaşamı tehdit ediyor.", file=discord.File(image))

@bot.command()
async def soru3(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\images.jpg"
    await ctx.send("Sanıldığı gibi iklim değişikliğinden etkilenenler sadece eriyen buzul bölgelerindeki kutup canlıları değil. Yaşanan değişim dünya üzerindeki tüm canlıları az veya çok etkiliyor. Birkaç örnek üzerinden gidelim: İnsanlığın çevreye verdiği zararlar kuşların göç yollarını değiştiriyor. Yumurtlamak için soğuk nehirlere muhtaç olan somonların nesli hızla tükeniyor. Ormansızlaşma yaban hayat türlerini riske atıyor. Isınan ve kirlenen okyanuslardaki hayvanlar tehlike altında. İklimle gelen tüm bu olumsuz etkilere orantısız ve hatalı avcılık da eklenince sorunlar büyüyor.", file=discord.File(image))

@bot.command()
async def soru4(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\küreselısınma.jpg"
    await ctx.send("İlk sorunun yanıtında da açıkladığımız gibi, insan kaynaklı değişim nihayetinde en çok insanı etkiliyor. Tarım alanları azalıyor ve kıtlık riski oluşuyor. Suyun orantısız kullanımı susuzluk çanlarının çalmasına neden oluyor. Aşırı hava olayları insanları göçe zorluyor. Dünyanın birçok yerinde deniz kıyısındaki yaşam bölgelerinin su seviyesinin yükselmesi nedeniyle tahliye edilmesi gerekiyor. Küresel ısınma en çok gelişmiş ülkelerin faaliyetlerinden kaynaklanırken, sonuçtan en çok yoksul ülkelerin etkileneceği yapılan birçok araştırma tarafından vurgulanıyor.", file=discord.File(image))

@bot.command()
async def soru5(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\iklim-degisikligi.jpg"
    await ctx.send("Dünyamızın dörtte üçünden fazlası sudan oluşuyor ve doğal olarak su, büyük oranda etkileniyor. Isınan okyanus sıcaklıkları kutup buzlarını eritiyor, okyanus akıntılarını ve balık göçlerini değiştiriyor, mercanların beyazlamasına ve yok olmasına neden oluyor. Okyanuslar, sera gazı emisyonlarını emerek Dünya'nın iklimini düzenlemedeki önemli rolü nedeniyle, iklim değişikliğinden doğrudan etkileniyor. Emilen yüksek miktardaki karbondioksit, okyanuslarımızın kimyasını değiştirerek onları daha asidik hale getiriyor. Bu da birçok deniz habitatını ve hayvanı olumsuz etkiliyor. Daha ötesi, okyanus yüzeyinin ısınması bazı canlı türlerinin yok olmasına sebep oluyor ve bu da tüm besin zincirini etkiliyor.", file=discord.File(image))

@bot.command()
async def soru6(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\aaa.png"
    await ctx.send("Sanılanın çok ötesinde… Ormanlar, en önemli doğal karbon depolama alanlarımızdan biri. Bu nedenle ormanlar azaldığında, sera gazını depolama yeteneklerini kaybederler. Yanan ağaçlar atmosfere daha fazla karbon salar. Ormansızlaşmayı yavaşlatabilir, durdurabilir ve doğal araziyi sağlıklı şekilde yönetebilirsek, küresel sıcaklıkların 2 °C'den fazla yükselmesini önlemek için 2030 yılına kadar ihtiyaç duyulan emisyon azaltımlarının üçte birine kadar ulaşabiliriz. Bu, dünyanın petrol kullanımını tamamen durdurmasına eşdeğer bir katkı anlamına geliyor.", file=discord.File(image))

@bot.command()
async def soru7(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\fotomu.jpg"
    await ctx.send("Yerküre, okyanuslar ve atmosferin, son 100 yıl içerisindeki insan aktiviteleriyle hava küreye karbondioksit, metan gibi sera gazlarının salımı sonucu (temel olarak fosil yakıtlar kullanmak suretiyle) ısınmaya başladığını biliyoruz. Küresel ısınmanın en açık göstergesinin, dünya sıcaklığının artması olduğu söylenebilir. Bunun sonucu olarak; başta buzulların erimesi, deniz seviyelerinin yükselmesi ve iklimlerin değişmesi beklenmektedir.Geçtiğimiz 100 yıllık süre içerisinde 1oC'e yakın bir sıcaklık artışı söz konusu.Buda dünyamızı aşırı derecede büyük bir tehdidle karşı karşıya kalması demektir.", file=discord.File(image))

@bot.command()
async def soru8(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\foto2.jpg"
    await ctx.send("Küresel iklim değişikliği sonucu önceden taşkın, kuraklık vb. olumsuzluklar görülmeyen bir bölgede bu tür sorunların yaşanması mümkün. Çok nadir sorunlar yaşanan bölgede daha sık sorunların yaşanması da mümkün. Esas itibarıyla, bir bölgede belli bir zamanda olağanüstü bir hal yaşanabilmesi için bir dış etki olması gerekir. Ancak, bu sorunun oluşturduğu zarar, sizin bu etkiye karşı direncinize ve duyarlılığınıza bağlı olarak şekillenir. Örneğin yağış azlığı sonucu kuraklık etkilerinin hissedilmesi, bu duruma karşı hazırlıklı olup olmadığımızla ilgili.Yeterince su depolayan rezervuarlarınız varsa, su tasarrufu sağlayan sistemlerinizi oluşturmuşsanız, yani arz talep dengesini yönetebiliyorsanız kuraklık etkilerinden olabildiğince az etkilenirsiniz. Diğer taraﬅ an, küresel iklim değişikliği sonucu beklenenin üzerinde sağanaklara karşı kentsel altyapınız hazır ise taşkın etkilerini çok daha az hissedersiniz. Dere veya taşkın yatağında yapılaşma olmayan, yağmur suyu drenaj sistemleri oluşturulmuş kentler veya yerleşim yerleri artan yağışın olumsuz etkilerden çok daha az etkilenecektir.", file=discord.File(image))

@bot.command()
async def soru9(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\foto3.jpg"
    await ctx.send("Suyun hidrolojik döngü içerisindeki zamansal ve konumsal hareketinin küresel iklim değişikliğiyle önemli ölçüde etkilendiğini, ekstrem olaylara ilişkin gözlemlere bakarak kolaylıkla görebiliyoruz. Özellikle, son 1 yıl içerisinde dünyanın bir noktasında şiddetli yağışlar ve taşkınlar, diğer bir noktasında susuzluk ve kuraklık yaşandığına şahitlik ediyoruz. Benzer şekilde, Güney Kutbu'nda rekor sıcaklıklar ve buzul erimeleri meydana gelirken, çöl ortasında sağanak yağışlar ve sel ile karşılaşabiliyoruz.Geldiğimiz noktada, suyun hem varlığının hem yokluğunun ciddi sorunlara yol açtığını söyleyebilirim. Bu nedenle, bir yandan iklim değişikliğine karşı küresel bazda sürekli ve kararlı uygulanabilecek tedbirler geliştirirken, diğer taraﬅ an yaşam alanlarımızı iklim değişikliğinin etkilerine karşı korunaklı hale getirmemiz gerekiyor.", file=discord.File(image))

@bot.command()
async def soru10(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\foto4.jpg"
    await ctx.send("11 Ağustos 2021 günü Kastamonu'nun Bozkurt ilçesinin bulunduğu havzada ve çevre havzalarda meydana gelen sel felaketleri sırasında gözlenen yağış miktarı Meteoroloji Genel Müdürlüğü verilerine göre yer yer 100 ila 300 mm arasında değişiyor. Türkiye ortalaması olan 760 mm yıllık toplam yağış temel alındığında, bir yaz gününde düşen yağışın ne kadar fazla olduğu açıkça görülebilir.Bununla birlikte, bu büyüklükteki bir yağış havza içerisinde baraj, sel kapanı vb. yapılarla üst akış kesitlerinde tutularak; yağış sonucu oluşan akış, ıslah çalışmalarıyla denetim altına alınarak veya taşkın yatağında yapılaşmayla izin verilmeyerek taşkın zararları en aza indirgenebilir.", file=discord.File(image))

@bot.command()
async def soru11(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\foto5.jpg"
    await ctx.send("Temmuz ayı verileriyle ülke genelinde son 60 yılın en az yağışı ile karşı karşıyayız. Dolayısıyla, meteorolojik kuraklığı baz aldığımızda son 60 yılın en kurak yılını yaşadığımızı söyleyebiliriz. Ancak, kuraklıktan etkilenme miktarımız kuraklığın tanımına ve de yerelde kuraklığa karşı ne kadar hazırlıklı olduğumuza bağlı olarak değişecektir. Örneğin, karasal su kaynaklarının durumunu ifade eden hidrolojik kuraklık dikkate alındığında; göl, baraj, akarsu, yeraltı suyu gibi bölgedeki su kaynaklarındaki azalma, kuraklığın şiddetini gösterecektir.Bu da dünyada su kıtlığına yol açabilir.", file=discord.File(image))

@bot.command()
async def soru12(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\foto6.jpg"
    await ctx.send("Birleşmiş Milletler Su Gelişim Raporu; Birleşmiş Milletler'in su konusunda her yıl farklı tema ile yayınladığı, dünya tatlı su kaynaklarının kapsamlı değerlendirmesini yapan dünyadaki en önemli küresel raporlardan biri. Bu yılki tema 'Mavi Altınımızın Gerçek Değerini Anlayalım' biçimde. Rapor özetle, suyun değerinin anlaşılamamasının sularımızınisrafının ana nedeni olduğunu ifade ediyor. Özellikle artan kuraklık, iklim değişikliği ve nüfus artışı yaşadığımız bir dönemde, suyun değerini kavrayabilmek suyun hayatımızdaki yerini tam olarak anlayabilmekle mümkün. Milyarlarca insanın doğrudan erişiminin olmadığı, dünyanın en değerli kaynağı olan su (mavi altın), sadece yaşamın kaynağı olmayıp, toplumun sağlığının, sosyal ve kültürel gelişiminin de temelidir.Rapor, suyun israf edilmesi ve verimsiz kullanılmasının, suyu sadece fiyatı üzerinden değerlendirmemizden ve hayati değerini anlamamızdan kaynaklandığını vurguluyor. Suyun yokluğunda suyun ücretini belirlemek imkânsız ve paha biçilmezdir.", file=discord.File(image))

@bot.command()
async def soru13(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\foto7.jpg"
    await ctx.send("İklimler astronomik ve atmosferik etkilere bağlı olarak şekillenir. Bu nedenle, yerkürenin konumu ve hareketine ve hava küredeki değişimlere bağlı olmak üzere; yerkürenin farklı konumları farklı zamanlarda farklı etkilere maruz kalır. Kütlenin korunumu yasası ve hidrolojik döngü gereği, yerküre ve hava küre etrafında dönen su miktarı, sıcaklık ve radyasyon değişimleri, basınç ve rüzgâr hareketleri ve diğer hidrolojik değişkenler, küresel bazda bir denge içerisindeler. Bu minvalde, doğamız yağışı buharlaşmayla, sıcağı soğukla, yüksek basıncı alçak basınçla dengelemeye çalışır. Ekstrem olaylar dikkate alındığında bu dengeleme arayışı kendini daha belirgin biçimde gösterir. Örneğin, bir yerde ve konumda kuraklık yaşanırken, başka bir zaman ve konumda taşkınların görülmesi ya da bir taraf sıcaklıktan kavrulurken diğer taraf da soğuktan donacak durumların gözlenmesi bu nedenledir.Doğanın insan faaliyetleri sonucu söz konusu bu dengeyi sağlayamaması durumunda yerel bazda yağış, akış, sıcaklık, nem gibi parametrelerde artış ve azalış formunda trendler gözlemek olasılık dâhilinde. Bu durumun, kaynak yönetiminin sağlanamadığı yerleşimlerde insan ve canlı hareketlerinin oluşmasına yol açması da muhtemel.", file=discord.File(image))

@bot.command()
async def soru14(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\foto8.jpg"
    await ctx.send("İklim değişikliğinin etkileri konuma, bölgesel duyarlılık ve direncinize bağlı olarak şekilleniyor. Bu nedenle, bölgesel duyarlılık ve dirençlerimize bağlı olarak etkin, entegre ve sürdürülebilir bir su kaynakları yönetimi gerçekleştirerek; genel, bölgesel ve yerel mücadele politikaları üretmek suretiyle, iklim değişikliğinin sonuçlarından daha az etkilenebiliriz.Bu anlamda, ilk yapmamız gereken şey, kaynaklarımızı etkin bir biçimde değerlendirmemize imkan sağlayacak mekanizmaları hayata geçirmektir.", file=discord.File(image))

@bot.command()
async def soru15(ctx):
    image="C:\\Users\\mehme\OneDrive\\Masaüstü\\kodland\\foto\\foto9.png"
    await ctx.send("İklim değişikliği, genellikle karmaşık bilgisayar modellemelerinin yaptığı bir tahmin olarak karşımıza çıkar. Fakat iklim değişikliğinin bilimsel temeli çok daha geniştir, modellemeler bu temelin yalnızca bir kısmını oluşturur (ki ilginç bir şekilde, bu modellemeler çok isabetlidir).Yüz yıldan uzun bir süredir bilim insanları, sera gazlarının ısınmaya sebebiyet vermesinin ardındaki temel fiziği anlamış bulunuyor. ", file=discord.File(image))

bot.run("Insert Your Own Token here")
