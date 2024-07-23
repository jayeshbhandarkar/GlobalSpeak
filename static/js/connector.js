

// console.log('out')
// document.querySelector('textarea').addEventListener('input', function (event) {
//     console.log(event.target.value);
// });
const form_text = document.getElementById('form_text')
if (form_text != null) {
    // form_text.addEventListener('submit', function (event) {
    form_text.addEventListener('submit', (event) => {
        event.preventDefault();    // prevent page from refreshing
        const formData = new FormData(form_text);  // grab the data inside the form fields
        console.log(formData.entries());
        let selected_lang = ''
        for (const pair of formData.entries()) {
            if (pair[0] == 'target_language') {
                selected_lang = pair[1]
                break;
            }
            console.log(`${pair[0]}, ${pair[1]}`);
        }
        let lang = document.querySelector('.language');
        lang.innerText = "Selected Language: " + `${selected_lang}`;
        fetch('/text_translate', {   // assuming the backend is hosted on the same server
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(json => {
                const language = document.querySelector('.language')
                // language.innerText += 
                const op = document.getElementById("text")
                let ans = json.text;
                op.innerText = ans
            });
    });
}


const form_audio = document.getElementById('form_audio')
if (form_audio != null) {
    form_audio.addEventListener('submit', (event) => {
        event.preventDefault();    // prevent page from refreshing
        const formData = new FormData(form_audio);  // grab the data inside the form fields
        console.log(formData.values());
        for (const pair of formData.entries()) {
            console.log(`${pair[0]}, ${pair[1]}`);
        }
        fetch('/audio_translate', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(json => {
                const op = document.getElementById("text_audio")
                let ans = json.text;
                op.innerText = ans
                const a = document.querySelector('.audio-output')
                // source.setAttribute('src', '../translated_audio/captured_voice.mp3"')
                a.innerHTML = `<audio class="converted-audio" controls="controls"> </audio > `
                console.log(a);

                const audio = document.querySelector('.converted-audio')
                console.log(audio);
                audio.innerHTML = "<source src = '..\\translated_audio\\captured_voice.mp3' type = 'audio/mpeg' >"
                console.log(audio);

            });
    });
}


const form_video = document.getElementById('form_video')
if (form_video != null) {
    form_video.addEventListener('submit', (event) => {
        event.preventDefault();
        const formData = new FormData(form_video);
        let selected_lang = ''
        for (const pair of formData.entries()) {
            if (pair[0] == 'target_language') {
                selected_lang = pair[1]
                break;
            }
            console.log(`${pair[0]}, ${pair[1]}`);
        }
        // let file = document.getElementById('file-selection');
        // file.innerText = 'File succesfully parsed';
        // let l = document.querySelector('#selected-lang');
        // l.innerText = "Selected Language: " + `${selected_lang}`;
        fetch('/video_translate', {
            method: 'POST',
            body: formData,
        })
            .then(responce => responce.json())
            .then(json => {
                console.log(json);
                const progress = document.getElementById('progress')
                progress.innerText = "Translation over"
                const inputVideo = document.getElementById('original')
                inputVideo.innerHTML = ` <video controls style="width: 95%;">
                            <source src="..\\audio_from_video\\original.mp4" type="video/mp4">
                        </video>`
                const translatedVideo = document.getElementById('translated-video')
                translatedVideo.innerHTML = `<video controls style="width: 95%;">
                                                <source src="..\\audio_from_video\\translated_video.mp4" type="video/mp4">
                                            </video>`
            })
    })
}