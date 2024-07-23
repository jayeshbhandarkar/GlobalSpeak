var languages = {
    "afrikaans": "af", "albanian": "sq", "arabic": "ar",
    "bengali": "bn", "bosnian": "bs", "bulgarian": "bg",
    "catalan": "ca", "cebuano": "ceb", "chichewa": "ny", "chinese (simplified)": "zh-cn", "chinese (traditional)": "zh-tw",
    "corsican": "co", "croatian": "hr", "czech": "cs", "danish": "da", "dutch": "nl",
    "english": "en", "esperanto": "eo", "estonian": "et", "filipino": "tl", "finnish": "fi",
    "french": "fr", "frisian": "fy", "galician": "gl", "georgian": "ka", "german": "de",
    "greek": "el", "gujarati": "gu", "haitian creole": "ht", "hausa": "ha", "hawaiian": "haw",
    "hebrew": "he", "hindi": "hi", "hmong": "hmn", "hungarian": "hu", "icelandic": "is",
    "igbo": "ig", "indonesian": "id", "irish": "ga", "italian": "it", "japanese": "ja",
    "javanese": "jw", "kannada": "kn", "kazakh": "kk", "khmer": "km", "korean": "ko",
    "kurdish (kurmanji)": "ku", "kyrgyz": "ky", "lao": "lo", "latin": "la", "latvian": "lv",
    "lithuanian": "lt", "luxembourgish": "lb", "macedonian": "mk", "malagasy": "mg", "malay": "ms",
    "malayalam": "ml", "maltese": "mt", "maori": "mi", "marathi": "mr", "mongolian": "mn",
    "myanmar (burmese)": "my", "nepali": "ne", "norwegian": "no", "odia": "or", "pashto": "ps",
    "persian": "fa", "polish": "pl", "portuguese": "pt", "punjabi": "pa", "romanian": "ro",
    "russian": "ru", "samoan": "sm", "scots gaelic": "gd", "serbian": "sr", "sesotho": "st",
    "shona": "sn", "sindhi": "sd", "sinhala": "si", "slovak": "sk", "slovenian": "sl",
    "somali": "so", "spanish": "es", "sundanese": "su", "swahili": "sw", "swedish": "sv",
    "tajik": "tg", "tamil": "ta", "telugu": "te", "thai": "th", "turkish": "tr",
    "ukrainian": "uk", "urdu": "ur", "uyghur": "ug", "uzbek": "uz", "vietnamese": "vi",
    "welsh": "cy", "xhosa": "xh", "yiddish": "yi", "yoruba": "yo", "zulu": "zu"
}

function createDatalist(datalist) {
    // const datalist = document.getElementById(id);
    console.log(datalist);
    const langs = Object.keys(languages);

    for (let index = 0; index < langs.length; index++) {
        var element = langs[index];
        // element = "value=" + element;
        // console.log(element);
        const listElement = document.createElement('option');
        listElement.innerHTML = element;
        datalist.append(listElement);

    }
}

const textLangList = document.getElementById('language-list-text')
const audioLangList = document.getElementById('language-list-audio')
const videoLangList = document.getElementById('language-list-video')

if (textLangList != null) {
    createDatalist(textLangList);
    // handleOnChange()
}

if (audioLangList != null) {
    createDatalist(audioLangList);
}

if (videoLangList != null) {
    createDatalist(videoLangList);
}
