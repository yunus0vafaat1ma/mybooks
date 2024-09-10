from django.shortcuts import HttpResponse


def book_list(request):
    response = """
        <h1>Kitoblar ro'yxati</h1>
        <a href="/book/1">
            <ul>
                <li>Imomning maniken qizi</li>
            </ul>
        </a>
        <a href="/book/2">
            <ul>
                <li>500 yildan so'ng</li>
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
        <p>Turkiya kichik qishlog‘ining imomi, uning oilasi va jonajon qizi Fotimaning taqdiri, hayot yo‘llari orqali bugungi juda ko‘p davlatlardagi vaziyatlar, ikkilanayotgan yoshlar taqdiri  ifodalangan ushbu asar og‘riqli nuqtalarni yodga soladi.
        Inson qanday bo‘lmasin o‘zligidan, asliyatidan voz kecha olmaydi. Qanday vaziyatda yashasa ham insoniyligini unutmasa bas. </p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(response)
def book(request):
    author = """
    <p>Emine Şenlikoğlu (1950-yil 1-yanvar, Giresun shahrida tugʻilgan) – turk tadqiqotchisi, yozuvchisi. Asl ismi Emine Oʻzjan Şenlikoğlu (Emine Özkan Şenlikoğlu)dir. U islomiy mazmundagi kitob va romanlar yozishi, konferensiyalaridagi nutqlari bilan mashhur.</p>
    <a href="../">Back to list</a>
    """
    return HttpResponse(author)


def book_list3(request):
    response = """
        <h1>500 yildan so'ng</h1>
        <a href="/book2">Author:</a>
        <p>Amina Shenlik o'glu</p>
        <p>Turk adibalaridan biri bo'lgan Omina Shenliko'g'li o'zining kutilmagan mavzudagi asarlarni bizga taqdim etishi bilan mashxurdir. Adibaning yana bir "500 yildan so'ng" asari  "Azon kitoblar" tomonidan ilk bor  nashr qilingan va  fantastik roman bo'lib ushbu asar hali turkiyada ham chop etilmagani bilan kitobxonni o'ziga jalb qila oladi.</p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(response)
def book2(request):
    author = """
    <p>Emine Şenlikoğlu (1950-yil 1-yanvar, Giresun shahrida tugʻilgan) – turk tadqiqotchisi, yozuvchisi. Asl ismi Emine Oʻzjan Şenlikoğlu (Emine Özkan Şenlikoğlu)dir. U islomiy mazmundagi kitob va romanlar yozishi, konferensiyalaridagi nutqlari bilan mashhur[2].</p>
    <a href="../">Back to list</a>
    """
    return HttpResponse(author)

def book_list4(request):
    response = """
        <h1>Iskanja</h1>
        <a href = "/book3">Author:</a>
        <p>Amina Shenlik o'glu</p>
        <p>Ushbu asarda kommunizm iskanjasi qurboniga aylangan bir Uygʼur millatiga mansub musulmon oilasining qismati yoritilgan. Kommunizm niqobi ostida millatning, yoshlarning ongiga maʼnaviyat, madaniyat deb dinsizlik gʼoyalarning singdirilishi, xalqni oʼzligidan, milliy va diniy ildizlaridan judo qilish jarayonlari yorqin ifodalab berilgani ushbu kitob kitobxonni befarq qoldirmasligi tabiiy.</p>
        <a href="../">Back to list</a>
    """
    return HttpResponse(response)

def book3(request):
    author = """
    <p>Emine Şenlikoğlu (1950-yil 1-yanvar, Giresun shahrida tugʻilgan) – turk tadqiqotchisi, yozuvchisi. Asl ismi Emine Oʻzjan Şenlikoğlu (Emine Özkan Şenlikoğlu)dir. U islomiy mazmundagi kitob va romanlar yozishi, konferensiyalaridagi nutqlari bilan mashhur</p>
    <a href="../">Back to list</a>
    """
    return HttpResponse(author)