from django.shortcuts import HttpResponse


def book_list(request):
    response = """
        <h1>Kitoblar ro'yhati</h1>
        <a href="/book/1">
            <ul>
                <li>Imomning maniken qizi</li>
            </ul>
        </a>
        <a href="/book/2">
            <ul>
                <li>O'tgan kunlar</li>
            </ul>
        </a>
        <a href="/book/3">
            <ul>
                <li>Iskanja</li>
            </ul>
        </a>
    """
    return HttpResponse(response)


def book_list2(request):
    response = """
        <h1>Imomning maniken qizi</h1>
        <a href="/book">Author:</a>
        <p>Amina Shenlik o'glu</p>
        <p>Agar imom ham qizi orzu qilganidek, televizor olib berganda, arg’umchoqlar uchishiga to’sqinlik qilmaganga, “Imomning qizisan” deb beg’ubor bolaligini tortib olmaganda, balki hayotlari boshqacha bo’larmidi</p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(response)
def book(request):
    author = """
        <p>Hayoti - Oʻtkir Hoshimov 1941-yilning 5-avgustida Toshkent viloyatining Zangiota tumani Doʻmbirobod mavzesida tavallud topgan. Bolaligi urush qiyinchiliklari, muhtojliklari davrida kechgan. 1958-yilda oʻrta maktabni bitirib, Toshkent Davlat universiteti jurnalistika boʻlimining avval sirtqi, soʻngra kunduzgi boʻlimida oʻqib, 1964-yilda tugatadi. </p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(author)


def book_list3(request):
    response = """
        <h1>Iskanja</h1>
        <a href="/book2">Author:</a>
        <p>Amina Shenlik o'glu</p>
        <p>„Iskanja“ – oʻzbek yozuvchisi Pirimqul Qodirov qalamiga mansub tarixiy roman. Asarda Zahiriddin Muhammad Bobur hayoti haqida soʻz yuritiladi. Qodirov mazkur roman ustida oʻn yil (1969—1978) davomida ish olib borgan[1]. „Yulduzli tunlar“ga „Boburnoma“ hamda „Humoyunnoma“ asarlari asosiy manba boʻlib xizmat qilgan.
            „Iskanja“ zamonaviy oʻzbek adabiyotining eng sara asarlaridan biri hisoblanadi[2].</p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(response)
def book2(request):
    author = """
    <p>Abdulla Qodiriy (asosiy taxalluslari: Qodiriy, Julqunboy) (1894.4.10-Toshkent-1938.10.4) – XX-asr yangi oʻzbek adabiyotining ulkan namoyandasi, oʻzbek romanchiligining asoschisi; 20-yillardagi muhim ijtimoiy-madaniy jarayonlarning faol ishtirokchisi. Bogʻbon oilasida tugʻilgan. Otasi Qodirbobo (1820—1924) xon, beklar qoʻlida sarbozlik qilgan, rus bosqini paytida (1865) Toshkent mudofaasida qatnashgan. Otasi boshidan oʻtgan sarguzashtlar Abdulla Qodiriyning qator asarlari, xususan tarixiy romanlarining yuzaga kelishida muhim rol oʻynagan</p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(author)

