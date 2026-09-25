// ==========================================
// INTELLEARN VOICE.JS
// ==========================================


// ==========================================
// GET PREFERRED LANGUAGE FROM FLASK
// ==========================================
//
// voice.html must contain:
//
// <script>
//     const speechLanguage = "{{ speech_language }}";
//     const preferredLanguage = "{{ preferred_language }}";
// </script>
//
// Flask should send:
//
// English -> en-IN
// Telugu  -> te-IN
// Hindi   -> hi-IN
//
// ==========================================

const selectedLanguage =
    (typeof speechLanguage !== "undefined" && speechLanguage)
        ? speechLanguage
        : "en-IN";


// ==========================================
// LANGUAGE-SPECIFIC MESSAGES
// ==========================================

const voiceMessages = {

    English: {
        listening: "🎤 Listening... Speak now",
        converted: "✅ Speech converted to text",
        again: "Click the microphone and speak again.",
        unsupported:
            "Speech recognition is not supported in this browser. Please use Google Chrome.",
        noText: "There is no text to read.",
        notFound: "Lesson text was not found.",
        error: "❌ Error: "
    },

    Telugu: {
        listening: "🎤 వింటోంది... ఇప్పుడు మాట్లాడండి",
        converted: "✅ మీ మాటలు టెక్స్ట్‌గా మార్చబడ్డాయి",
        again: "మైక్రోఫోన్‌ను క్లిక్ చేసి మళ్లీ మాట్లాడండి.",
        unsupported:
            "ఈ బ్రౌజర్‌లో స్పీచ్ రికగ్నిషన్‌కు మద్దతు లేదు. దయచేసి Google Chrome ఉపయోగించండి.",
        noText: "చదవడానికి ఎలాంటి వచనం లేదు.",
        notFound: "పాఠం కనుగొనబడలేదు.",
        error: "❌ లోపం: "
    },

    Hindi: {
        listening: "🎤 सुन रहा है... अब बोलें",
        converted: "✅ आपकी आवाज़ को टेक्स्ट में बदल दिया गया है",
        again: "माइक्रोफ़ोन पर क्लिक करें और फिर से बोलें।",
        unsupported:
            "इस ब्राउज़र में स्पीच रिकग्निशन समर्थित नहीं है। कृपया Google Chrome का उपयोग करें।",
        noText: "पढ़ने के लिए कोई टेक्स्ट नहीं है।",
        notFound: "पाठ नहीं मिला।",
        error: "❌ त्रुटि: "
    }

};


// ==========================================
// GET CURRENT PREFERRED LANGUAGE
// ==========================================

let currentPreferredLanguage = "English";

if (
    typeof preferredLanguage !== "undefined" &&
    preferredLanguage
) {
    currentPreferredLanguage = preferredLanguage;
}


// ==========================================
// GET MESSAGES
// ==========================================

const messages =
    voiceMessages[currentPreferredLanguage]
        || voiceMessages["English"];


// ==========================================
// SPEECH TO TEXT
// ==========================================

function startSpeechRecognition() {

    // --------------------------------------
    // CHECK BROWSER SUPPORT
    // --------------------------------------

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;


    if (!SpeechRecognition) {

        alert(messages.unsupported);

        return;
    }


    // --------------------------------------
    // CREATE RECOGNITION OBJECT
    // --------------------------------------

    const recognition =
        new SpeechRecognition();


    // --------------------------------------
    // RECOGNITION SETTINGS
    // --------------------------------------

    recognition.continuous = false;

    recognition.interimResults = false;

    // IMPORTANT:
    // Use preferred language for speech recognition

    recognition.lang = selectedLanguage;


    // --------------------------------------
    // WHEN LISTENING STARTS
    // --------------------------------------

    recognition.onstart = function () {

        const status =
            document.getElementById("voiceStatus");

        if (status) {

            status.innerText =
                messages.listening;

        }
    };


    // --------------------------------------
    // WHEN SPEECH IS RECOGNIZED
    // --------------------------------------

    recognition.onresult = function (event) {

        const speechText =
            event.results[0][0].transcript;


        const textBox =
            document.getElementById("speechText");


        if (textBox) {

            textBox.value =
                speechText;
        }


        const status =
            document.getElementById("voiceStatus");


        if (status) {

            status.innerText =
                messages.converted;
        }
    };


    // --------------------------------------
    // WHEN RECOGNITION ENDS
    // --------------------------------------

    recognition.onend = function () {

        const status =
            document.getElementById("voiceStatus");


        if (status) {

            status.innerText =
                messages.again;
        }
    };


    // --------------------------------------
    // ERROR HANDLING
    // --------------------------------------

    recognition.onerror = function (event) {

        const status =
            document.getElementById("voiceStatus");


        if (status) {

            status.innerText =
                messages.error +
                event.error;
        }
    };


    // --------------------------------------
    // START RECOGNITION
    // --------------------------------------

    try {

        recognition.start();

    } catch (error) {

        console.error(
            "Speech recognition error:",
            error
        );
    }
}


// ==========================================
// TEXT TO SPEECH
// ==========================================

function speakText() {

    // --------------------------------------
    // FIND LESSON TEXT
    // --------------------------------------

    const lessonElement =
        document.getElementById("lessonText");


    if (!lessonElement) {

        alert(messages.notFound);

        return;
    }


    // --------------------------------------
    // GET TEXT
    // --------------------------------------

    const text =
        lessonElement.innerText.trim();


    // --------------------------------------
    // CHECK EMPTY TEXT
    // --------------------------------------

    if (text === "") {

        alert(messages.noText);

        return;
    }


    // --------------------------------------
    // CREATE SPEECH
    // --------------------------------------

    const speech =
        new SpeechSynthesisUtterance(text);


    // IMPORTANT:
    // Use preferred language

    speech.lang =
        selectedLanguage;


    // --------------------------------------
    // SPEECH SETTINGS
    // --------------------------------------

    speech.rate = 0.9;

    speech.pitch = 1;

    speech.volume = 1;


    // --------------------------------------
    // STOP PREVIOUS SPEECH
    // --------------------------------------

    window.speechSynthesis.cancel();


    // --------------------------------------
    // SPEAK
    // --------------------------------------

    window.speechSynthesis.speak(
        speech
    );
}