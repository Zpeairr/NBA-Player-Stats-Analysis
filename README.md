# NBA-Player-Stats-Analysis
Projenin Amacı:
Bu proje, 2023-24 NBA sezonu oyuncu istatistiklerini analiz ederek yaş, oynama süresi ve başarılı şut yüzdesi (FG%) arasındaki ilişkiyi incelemeyi amaçlamaktadır. Araştırmada, yaş ve oynama süresinin şut başarısını etkileyip etkilemediği ve bu değişkenler arasında anlamlı bir ilişkinin olup olmadığı araştırılmıştır.

Araştırma Sorusu:
Yaş, oynama süresi ve başarılı şut yüzdesi (FG%) arasındaki ilişki nedir? Bu faktörler arasında anlamlı bir etkileşim var mıdır?

Veri Toplama Yöntemi:
Veriler, NBA’nin resmi web sitesinden Selenium kütüphanesi kullanılarak otomatik bir web kazıma yöntemiyle elde edilmiştir. Oyuncuların temel performans istatistikleri, özellikle yaş, oynama süresi ve FG% değişkenleri incelenmiştir.

Veri Analizi
Tanımlayıcı İstatistikler ve Görselleştirmeler:

Başarılı Şut Yüzdesi Dağılımı:
Başarılı şut yüzdesinin histogramı incelenmiştir. Dağılımın yoğun olduğu aralıklar görselleştirilmiştir.

Yaşa Göre Başarılı Şut Yüzdesi:
Scatter plot ile yaş ve FG% arasındaki ilişki görselleştirilmiştir. Yaşa göre FG%’nin genel eğilimini görmek için bir çizgi grafik oluşturulmuştur.

Korelasyon Analizi:
Yaş, oynama süresi ve FG% değişkenleri arasındaki ilişki bir korelasyon matrisi kullanılarak incelenmiştir. Korelasyon katsayıları şu şekildedir:

Yaş ve FG%: 0.12 (düşük düzeyde pozitif ilişki)
Oynama Süresi ve FG%: 0.35 (orta düzeyde pozitif ilişki)
Gruplar Arası Analizler:
Yaş ve oynama süresine göre kategorize edilmiş gruplar arasındaki farklar bir boxplot ile görselleştirilmiştir.

Hipotez Testleri ve Sonuçları:

ANOVA Testi:
ANOVA analizi, yaş grubu, oynama süresi grubu ve bu iki faktörün etkileşiminin FG% üzerindeki etkisini incelemek için yapılmıştır.
Yaş Grubu: Anlamlı bir etki göstermemiştir (p > 0.05).
Oynama Süresi Grubu: Anlamlı bir etki göstermiştir (p < 0.05).
Yaş Grubu ve Oynama Süresi Grubu Etkileşimi: Anlamlı bir etki göstermemiştir (p > 0.05).
Sonuçlar ve Yorumlar
Analiz Sonuçlarının Yorumu:
Yaşın başarılı şut yüzdesi üzerinde doğrudan anlamlı bir etkisi olmadığı gözlemlenmiştir. Bununla birlikte, oynama süresi ile FG% arasında orta düzeyde pozitif bir ilişki bulunmaktadır. Bu durum, oyuncuların daha fazla süre aldıklarında performanslarını daha iyi yansıtabildiklerini göstermektedir.

Bulguların Önemi:
Bu analiz, NBA oyuncularının performans analizine dair karar verme süreçlerinde yaş yerine oynama süresinin daha güçlü bir metrik olduğunu göstermiştir.

Kaynakça
NBA Resmi Web Sitesi: https://www.nba.com/stats
Kullanılan Python Kütüphaneleri:
Selenium
Pandas
Matplotlib
Seaborn
Statsmodels
