const recordBtnStates = {
    'record': 'Start recording',
    'recording': 'Recording voice'
}

const recordBtnStyles = {
    'Start recording': `background-color: white;
                        border: 2px solid red;
                        color: black;`,
    'Recording voice': `background-color: red;
                        border: 2px solid white;
                        color: white;`,
}

const handleRecordClick = () => {
    const recBtn = document.getElementById('record-btn')
    if (recBtn.innerText === 'Start recording' || recBtn.innerText === 'Record') {
        recBtn.innerText = recordBtnStates.recording
    } else {
        recBtn.innerText = recordBtnStates.record
    }
    console.log(recBtn.innerText);
    let style = recordBtnStyles[recBtn.innerText]
    console.log(style);
    recBtn.setAttribute('style', style);
    const rowLengthHandler = document.querySelectorAll('.row')
    if (rowLengthHandler != null) {
        for (let i = 0; i < rowLengthHandler.length; i++) {
            const element = rowLengthHandler[i];
            element.innerHTML = ''
        }
    }
}

const handleVideoSubmittion = () => {
    const inputVideo = document.getElementById('original')
    inputVideo.innerHTML = ''
    const outputVideo = document.getElementById('translated-video')
    outputVideo.innerHTML = ''
    const progress = document.getElementById('progress')
    progress.innerText = "Translating"
}

const handleTextSubmittion = () => {
    const text = document.getElementById('text')
    text.innerText = ''
}

const handleTextCopy = () => {

    // Copy text in id text to clipboard
    let text = document.getElementById('text')
    text = text.innerText
    // text.select()
    // text.setSelectionRange(0, 99999)
    console.log(text);
    // document.execCommand('copy')
    navigator.clipboard.writeText(text);
    alert("Copied the text successfully!");
}