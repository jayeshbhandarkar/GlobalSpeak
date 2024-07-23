import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import time

text1 = ""
text2 = ""
def text_translator(text, target):
    """Trasnlate given text to target language

    Args:
        text (str): text to be translated
        target (str): target language

    Returns:
        str: translated text
    """
    startTime = time.time_ns()
    # if target not in languages.keys():
    #     return "Choose a valid language. Look in the Supported Languages list for more information"

    # target = languages[target].lower()
    translator = Translator()
    translation = translator.translate(text, dest=target)
    translated_text = translation.text
    # print(target)
    # print(translation.text)

    endTime = time.time_ns()
    print(endTime - startTime)
    # time = 784576000
    # return translated_text
    global text1
    text1 = translated_text
    return {'text': translated_text}

def translate2(text, target):
    startTime = time.time_ns()
    # if target not in languages.keys():
    #     return "Choose a valid language. Look in the Supported Languages list for more information"

    # target = languages[target].lower()
    translator = Translator()
    j = 0
    l = len(text)
    translated_text = ""
    while j + 100 < l:
        temptext = text[j : j + 100]
        translation = translator.translate(temptext, dest=target)
        translated_text += translation.text
        j += 100
    # translation = translator.translate(text, dest=target)
    # translated_text = translation.text
    # print(target)
    # print(translation.text)

    temptext = text[j:]
    translation = translator.translate(temptext, dest=target)
    translated_text += translation.text

    endTime = time.time_ns()
    print(endTime - startTime)
    global text2
    text2 = translated_text
    # time = 784576000
    # return translated_text
    return {'text': translated_text}

text = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptate autem, nam reprehenderit earum tempora non doloribus iure officiis obcaecati aspernatur qui molestiae, impedit, ea totam. Voluptate officia, perspiciatis cum neque quaerat ad nemo molestias! Doloremque quo unde deleniti, sunt fuga nostrum voluptate quam aperiam molestias perspiciatis maxime reiciendis laborum quod aliquam earum! Tenetur neque fugit quisquam consectetur impedit nostrum veniam expedita ducimus illum dignissimos ipsam, placeat, incidunt illo fugiat iste temporibus aliquam vel adipisci sequi, est provident ea? Eaque nulla suscipit minus sit ducimus est accusantium sequi magnam ex officia necessitatibus maxime, quia aliquid, sunt eum hic debitis iusto non repellendus vero nobis aut. Nihil omnis laudantium laborum repellat repudiandae dignissimos est, iure corrupti labore quaerat nisi dolorum, accusamus amet mollitia. Fuga, ipsa repellendus expedita nisi autem, in, blanditiis optio recusandae velit architecto itaque voluptates vel vitae consequuntur inventore veniam voluptatem? Consequatur unde nobis, nihil dolorum delectus eum fuga nesciunt provident commodi, labore eveniet magni praesentium? Molestias quae repellat autem eius dignissimos. Minus accusantium laudantium illo voluptatum placeat illum cupiditate excepturi praesentium eius atque nisi, ad quia eligendi asperiores! Veritatis in reprehenderit doloribus voluptate accusantium libero, harum error soluta animi laborum consequuntur vero earum neque, assumenda, reiciendis quis ratione quos tempora expedita aut. Adipisci recusandae, ipsam nihil distinctio minus nesciunt tempore ratione iure, deleniti doloremque natus perferendis. Eaque voluptatum accusamus qui magni soluta delectus labore, possimus numquam neque aut laudantium similique tenetur quidem, exercitationem doloremque blanditiis iste! Quaerat, et enim ullam cum magnam iste aut deleniti a numquam nam at! Quam eaque sunt nostrum, ea minus rem laudantium in expedita quos, sed a sapiente doloribus consequatur eius nulla nesciunt soluta. Maiores omnis aspernatur dolore accusantium? Cum voluptatibus quae quisquam temporibus numquam voluptates ea nesciunt atque repellat inventore itaque fuga, similique aliquam repudiandae modi architecto mollitia corrupti porro a. Soluta laborum temporibus veritatis ea iste laboriosam ratione quis? Officia dolorem ratione quam aliquid, nemo voluptas, tenetur sed eius modi similique exercitationem voluptatem officiis ipsa iusto magni praesentium aperiam laudantium repudiandae magnam neque eveniet. Error veritatis, blanditiis harum, quo velit voluptatibus magni quam neque earum excepturi animi itaque labore. Dicta autem nostrum tempora sunt molestiae. Doloribus adipisci nobis ipsam fuga. Quaerat pariatur eaque eius facilis accusamus fuga commodi natus placeat quisquam omnis ipsa doloribus earum, autem culpa incidunt optio voluptate suscipit expedita necessitatibus fugiat. Vel est, ad pariatur aut expedita consequatur error beatae voluptate nostrum sunt itaque distinctio! Aliquid cumque at magnam praesentium possimus vel ut nobis laboriosam architecto totam eveniet nulla vero voluptatem tempora beatae, molestias blanditiis voluptates fuga. Asperiores doloribus voluptatem corporis modi nam. At doloremque doloribus veniam dignissimos, culpa dolorem ut repellendus ullam cupiditate quod incidunt deserunt? Voluptatibus placeat nisi culpa provident quasi libero obcaecati eos porro omnis ipsam nemo corporis ad ratione sunt quisquam, vitae, saepe veniam doloremque commodi repudiandae nulla quos itaque soluta ea? Illo totam reprehenderit aliquid, accusamus distinctio, doloribus ducimus tempore accusantium atque corporis, perferendis reiciendis laborum odit. Cum praesentium unde, accusantium iusto et asperiores ex possimus obcaecati iste repudiandae ipsa! Qui vero quam totam doloremque tempora dolor corporis perspiciatis esse aliquam vitae! Soluta, in eaque omnis dolorem architecto magni est iusto corporis, hic quaerat quia sed nihil reiciendis. Error, voluptatibus fugit deleniti possimus blanditiis iure. Quam quas quaerat provident! In pariatur, hic facilis delectus repellat similique natus facere culpa dolor aperiam ducimus dolore doloribus libero dicta ea perspiciatis temporibus dignissimos architecto aliquam molestias. Nulla adipisci veniam animi magnam excepturi, quibusdam inventore beatae exercitationem esse ratione architecto? Hic impedit quibusdam blanditiis rerum nulla rem perspiciatis pariatur? Nisi nam odit possimus? Totam rem quasi perspiciatis, ducimus maiores repellat placeat ea tempora blanditiis dolor, alias modi numquam optio perferendis. Fugiat est earum voluptas quo, asperiores vero dolorum commodi corporis odio fugit ratione ipsam repellat. Vitae libero repudiandae, beatae, accusantium at recusandae, ab sit incidunt autem laborum tempore non. Dignissimos soluta enim quisquam corrupti ut dicta distinctio voluptas quis nobis id necessitatibus commodi, libero repudiandae debitis beatae delectus ab odit ducimus culpa voluptatem eum sint iusto. Totam ullam numquam incidunt aut sint dolore, nam veniam fuga omnis molestias tenetur. Tenetur, expedita. Aliquid qui ipsum quasi voluptatum accusamus dolorum, dolore maiores sint id, quibusdam quis reiciendis officiis hic! Id perspiciatis praesentium repudiandae a. Ab, ducimus quo repellendus quam dolores at magni explicabo tenetur aperiam quidem aliquam quasi accusantium dolorum rerum sint dicta recusandae accusamus atque expedita modi esse. Odio quo repellat aliquid obcaecati, id vel repudiandae enim provident assumenda ipsum fuga ratione nostrum odit corrupti veniam earum qui molestias molestiae incidunt atque ab maxime aliquam culpa? Assumenda voluptate libero dignissimos praesentium molestiae quibusdam recusandae ipsum architecto ratione maiores, dolores possimus illo optio impedit, incidunt quas iure, fugit mollitia amet nam voluptatem! Asperiores repudiandae necessitatibus consequuntur qui reiciendis voluptates blanditiis iusto labore illo unde! Veritatis rem natus fugiat explicabo, maxime distinctio, recusandae tenetur iusto sed in debitis asperiores iure consectetur expedita, sunt ad. Soluta, velit pariatur? Vitae placeat inventore illum commodi culpa ratione earum reprehenderit provident minima eveniet quaerat, amet debitis adipisci. Numquam asperiores excepturi quo voluptatem, quibusdam animi voluptatibus dolore nesciunt, earum error amet autem non quia harum doloribus illum corrupti quidem eligendi iure. Accusamus temporibus odio veritatis veniam sunt quae neque perferendis soluta quidem rem fugit dolore dolorum corporis animi provident id quam tenetur, minus ducimus? Fugiat sapiente dignissimos officia assumenda laudantium vitae! Vel soluta a eos suscipit quas ut, rem autem quam officiis? Laborum eius maiores, temporibus cupiditate quidem architecto eveniet quo vel sit explicabo unde deleniti, expedita perspiciatis quibusdam nobis officia. Et quo alias molestias quisquam odio, mollitia temporibus nesciunt numquam incidunt, quos, officiis obcaecati ipsum accusamus fugiat debitis iusto consequatur id tenetur quae? Error, modi porro odio officia suscipit maxime eligendi vel consectetur totam rem minima tenetur in tempore hic nemo ducimus. Numquam veritatis ea amet ullam repellat quibusdam? Quis harum, perferendis aliquid pariatur adipisci dolorem aliquam sit deleniti nam, corporis inventore illum laborum. Dolores explicabo, quis distinctio provident optio quo natus voluptatum, cum fugiat corrupti pariatur. Quasi impedit error fuga optio autem cupiditate, iusto minima! Dolore enim quam magni, fugiat reiciendis autem numquam quod."

text_translator(text, "hi")
translate2(text, "hi")
print(text1 == text2)
