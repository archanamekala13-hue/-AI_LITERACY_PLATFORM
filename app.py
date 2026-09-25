from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import sqlite3
import os
import shutil
from datetime import datetime


# =========================================================
# FLASK CONFIGURATION
# =========================================================

app = Flask(__name__)

app.secret_key = "intellilearn_secret_key"

DATABASE = "database.db"


# =========================================================
# TRANSLATIONS
# =========================================================

TRANSLATIONS = {

    # =====================================================
    # ENGLISH
    # =====================================================

    "English": {

        # Navigation
        "home": "Home",
        "dashboard": "Dashboard",
        "learn": "Learn",
        "voice": "Voice",
        "progress": "Progress",
        "profile": "Profile",
        "logout": "Logout",
        "register": "Register",
        "login": "Login",

        # Welcome
        "welcome": "Welcome to IntelliLearn",
        "welcome_back": "Welcome Back",
        "ready": "Ready to continue your learning journey?",

        # Progress
        "learning_progress": "Learning Progress",
        "overall_progress": "Overall Progress",
        "reading_progress": "Reading Progress",
        "writing_progress": "Writing Progress",
        "speaking_progress": "Speaking Progress",
        "keep_going": "Keep going! You are doing great.",

        # Learning Path
        "learning_path": "Your Learning Path",
        "complete_lessons": "Complete lessons to improve your skills.",

        # Skills
        "reading": "Reading",
        "writing": "Writing",
        "speaking": "Speaking",

        # Lessons
        "alphabet": "Alphabet",
        "alphabet_basics": "Alphabet Basics",
        "alphabet_description":
            "Learn the basic letters and their sounds.",

        "basic_words": "Basic Words",
        "basic_words_description":
            "Learn common everyday words.",

        "sentences": "Sentences",
        "simple_sentences": "Simple Sentences",
        "simple_sentences_description":
            "Practice reading and understanding simple sentences.",

        # Learn Page
        "choose_lesson": "Choose a Lesson",
        "lesson_label": "Lesson",
        "practice": "Practice",
        "daily_challenge": "Daily Learning Challenge",
        "daily_challenge_description": "Complete today's assessment and earn XP to improve your level.",
        "beginner_level": "Beginner Level",

        # Buttons
        "start": "Start",
        "continue_learning": "Continue Learning",
        "next": "Next",
        "back": "Back",
        "submit": "Submit",
        "save": "Save",

        # Dashboard
        "day_streak": "Day Streak",
        "total_xp": "Total XP",
        "current_level": "Current Level",

        # Voice
        "voice_practice": "Voice Practice",
        "start_speaking": "Start Speaking",
        "voice_title": "Speaking Practice",
        "voice_instruction":
            "Listen to the sentence and repeat it clearly.",
        "voice_sentence": "Practice Sentence",
        "listen": "Listen",
        "stop_speaking": "Stop Speaking",
        "voice_ready": "Ready to listen",
        "voice_listening": "Listening...",
        "voice_result": "Your voice has been recorded.",

        # Profile
        "choose_skill": "Choose a Skill",
        "my_profile": "My Profile",
        "edit_profile": "Edit Profile",
        "full_name": "Full Name",
        "email": "Email",
        "password": "Password",
        "preferred_language": "Preferred Language",
        "learning_language": "Learning Language",

        # Progress Page
        "progress_title": "My Progress",
        "progress_subtitle": "Track your learning journey.",
        "completed": "completed",

        # Assessment
        "assessment": "Initial Assessment",
        "assessment_title": "Initial Assessment",
        "assessment_instruction":
            "Answer the questions to understand your current learning level.",
        "submit_assessment": "Submit Assessment",
        "assessment_result": "Assessment Result",
        "your_score": "Your Score",
        "proficiency_level": "Proficiency Level",
        "beginner": "Beginner",
        "intermediate": "Intermediate",
        "advanced": "Advanced",
        "assessment_complete":
            "Assessment completed successfully!",
        "start_learning": "Start Learning",

        # Lesson
        "question": "Question",
        "of": "of",
        "correct": "Correct!",
        "incorrect": "Incorrect",
        "explanation": "Explanation",
        "continue": "Continue",
        "lesson_complete": "Lesson Complete!",
        "excellent": "Excellent work!",
        "good_job": "Good job! Keep practicing.",
        "keep_practicing": "Practice again to improve.",
        "score": "Score",
        "xp_earned": "XP Earned",
        "back_to_learning": "Back to Learning",
        "learning_games": "Learning Games",
        "sentence_builder_game": "Sentence Builder",
"sentence_builder_description": "Arrange the words and build a correct sentence.",

"speed_spell_game": "Speed Spell",
"speed_spell_description": "Type the word correctly before the timer runs out.",

"picture_match_game": "Picture Match",
"picture_match_description": "Match the picture with the correct word.",

"missing_word_game": "Missing Word",
"missing_word_description": "Choose the correct word to complete the sentence.",

"word_search_game": "Word Search",
"word_search_description": "Find the correct learning word in the grid.",

"picture_puzzle_game": "Picture Puzzle",
"picture_puzzle_description": "Look at the picture and arrange the word pieces.",
"practice_play": "Practice & Play",
"word_match_game": "Word Match",
"word_match_description": "Match each word with its correct meaning.",
"word_scramble_game": "Word Scramble",
"word_scramble_description": "Unscramble the letters and find the word.",
"memory_match_game": "Memory Match",
"memory_match_description": "Match pictures with their correct words.",
"listen_choose_game": "Listen & Choose",
"listen_choose_description": "Listen carefully and choose the correct word.",
"five_questions": "5 Questions",
"five_rounds": "5 Rounds",
"start_game": "Start Game",
"question_of": "Question",
"round_of": "Round",
"score": "Score",
"correct_great_job": "Correct! Great job!",
"correct_match": "Correct match! Excellent!",
"correct_listening": "Correct listening!",
"not_quite": "Not quite.",
"correct_answer": "Correct answer",
"not_a_match": "Not a match. Try the next round!",
"unscramble_word": "Unscramble the word",
"type_answer": "Type your answer",
"submit_answer": "Submit Answer",
"find_matching_pair": "Match the picture with the correct word",
"memory_instruction": "Click two cards and find their matching pair.",
"listen_correct_word": "Listen and choose the correct word",
"listen_again": "Listen Again",
"completed": "Completed",
"success": "Success!",
"excellent_memory": "Excellent Memory!",
"keep_improving": "Keep Improving!",
"play_again": "Play Again",
"close_game": "Close Game",
"excellent_word_knowledge": "Excellent work! Your word knowledge is strong.",
"practice_words": "Good attempt! Practice the words again to improve your score.",
"excellent_scramble": "Amazing! You solved the scrambled words very well.",
"practice_spelling": "Practice spelling and try the game again.",
"excellent_memory_message": "Great job! Your memory and vocabulary skills are developing very well.",
"practice_memory": "Keep practicing matching pictures and words to improve your memory.",
"excellent_listening": "Excellent listening! You identified the words correctly.",
"practice_listening": "Listen carefully and practice again to improve your listening skills.",
"please_enter_answer": "Please enter an answer.",
"learning_games": "Learning Games",
"practice_play": "Practice & Play",
"word_match_game": "Word Match",
"word_match_description": "Match each word with its correct meaning.",
"word_scramble_game": "Word Scramble",
"word_scramble_description": "Unscramble the letters and find the word.",
"memory_match_game": "Memory Match",
"memory_match_description": "Match pictures with their correct words.",
"listen_choose_game": "Listen & Choose",
"listen_choose_description": "Listen carefully and choose the correct word.",
"five_questions": "5 Questions",
"five_rounds": "5 Rounds",
"start_game": "Start Game",
"unscramble_word": "Unscramble the word",
"find_matching_pair": "Match the picture with the correct word",
"memory_instruction": "Click two cards and find their matching pair.",
"listen_correct_word": "Listen and choose the correct word",
"listen_again": "Listen Again",
"submit_answer": "Submit Answer",
"play_again": "Play Again",
"close_game": "Close Game",
"success": "Success!",
"keep_improving": "Keep Improving!",

        # Footer
        "footer": "Learn • Practice • Improve"
    },


    # =====================================================
    # TELUGU
    # =====================================================

    "Telugu": {

        "home": "హోమ్",
        "dashboard": "డ్యాష్‌బోర్డ్",
        "learn": "నేర్చుకోండి",
        "voice": "వాయిస్",
        "progress": "పురోగతి",
        "profile": "ప్రొఫైల్",
        "logout": "లాగ్ అవుట్",
        "register": "నమోదు",
        "login": "లాగిన్",

        "welcome": "IntelliLearn కు స్వాగతం",
        "welcome_back": "తిరిగి స్వాగతం",
        "ready":
            "మీ అభ్యాస ప్రయాణాన్ని కొనసాగించడానికి సిద్ధంగా ఉన్నారా?",

        "learning_progress": "అభ్యాస పురోగతి",
        "overall_progress": "మొత్తం పురోగతి",
        "reading_progress": "చదవడం పురోగతి",
        "writing_progress": "రాయడం పురోగతి",
        "speaking_progress": "మాట్లాడటం పురోగతి",
        "keep_going":
            "కొనసాగించండి! మీరు చాలా బాగా చేస్తున్నారు.",

        "learning_path": "మీ అభ్యాస మార్గం",
        "complete_lessons":
            "మీ నైపుణ్యాలను మెరుగుపరచడానికి పాఠాలను పూర్తి చేయండి.",

        "reading": "చదవడం",
        "writing": "రాయడం",
        "speaking": "మాట్లాడటం",

        "alphabet": "అక్షరమాల",
        "alphabet_basics": "అక్షరమాల ప్రాథమికాలు",
        "alphabet_description":
            "ప్రాథమిక అక్షరాలు మరియు వాటి శబ్దాలను నేర్చుకోండి.",

        "basic_words": "ప్రాథమిక పదాలు",
        "basic_words_description":
            "రోజువారీ ఉపయోగించే సాధారణ పదాలను నేర్చుకోండి.",

        "sentences": "వాక్యాలు",
        "simple_sentences": "సులభమైన వాక్యాలు",
        "simple_sentences_description":
            "సులభమైన వాక్యాలను చదవడం మరియు అర్థం చేసుకోవడం సాధన చేయండి.",

        "choose_lesson": "పాఠాన్ని ఎంచుకోండి",
        "lesson_label": "పాఠం",
        "practice": "అభ్యాసం",
        "daily_challenge": "రోజువారీ అభ్యాస సవాలు",
        "daily_challenge_description": "ఈ రోజు అంచనాను పూర్తి చేసి XP సంపాదించి మీ స్థాయిని మెరుగుపరచండి.",
        "beginner_level": "ప్రారంభ స్థాయి",

        "start": "ప్రారంభించండి",
        "continue_learning": "అభ్యాసాన్ని కొనసాగించండి",
        "next": "తదుపరి",
        "back": "వెనుకకు",
        "submit": "సమర్పించండి",
        "save": "సేవ్ చేయండి",

        "day_streak": "రోజుల స్ట్రీక్",
        "total_xp": "మొత్తం XP",
        "current_level": "ప్రస్తుత స్థాయి",

        "voice_practice": "వాయిస్ సాధన",
        "start_speaking": "మాట్లాడటం ప్రారంభించండి",
        "voice_title": "మాట్లాడే సాధన",
        "voice_instruction":
            "వాక్యాన్ని వినండి మరియు స్పష్టంగా పునరావృతం చేయండి.",
        "voice_sentence": "సాధన వాక్యం",
        "listen": "వినండి",
        "stop_speaking": "మాట్లాడటం ఆపండి",
        "voice_ready": "వినడానికి సిద్ధంగా ఉంది",
        "voice_listening": "వింటోంది...",
        "voice_result": "మీ వాయిస్ రికార్డ్ చేయబడింది.",

        "choose_skill": "నైపుణ్యాన్ని ఎంచుకోండి",
        "my_profile": "నా ప్రొఫైల్",
        "edit_profile": "ప్రొఫైల్ సవరించండి",
        "full_name": "పూర్తి పేరు",
        "email": "ఇమెయిల్",
        "password": "పాస్‌వర్డ్",
        "preferred_language": "ఇష్టమైన భాష",
        "learning_language": "నేర్చుకునే భాష",

                # Profile Page
        "profile_welcome":
            "మీ ప్రొఫైల్ మరియు అభ్యాస వివరాలను చూడండి.",

        "learner_profile":
            "అభ్యాసకుడి ప్రొఫైల్",

        "personal_information":
            "వ్యక్తిగత సమాచారం",

        "learning_statistics":
            "అభ్యాస గణాంకాలు",

        "learning_goal":
            "అభ్యాస లక్ష్యం",

        "learning_goal_description":
            "మీ అభ్యాస ప్రయాణాన్ని కొనసాగిస్తూ మీ నైపుణ్యాలను మెరుగుపరచుకోండి.",

        "beginner_journey":
            "ప్రారంభ అభ్యాస ప్రయాణం",

        "completed_percent":
            "పూర్తయింది",

        "learner":
            "అభ్యాసకుడు",

        "progress_title": "నా పురోగతి",
"progress_subtitle": 
    "మీ అభ్యాస ప్రయాణాన్ని ట్రాక్ చేయండి.",

"my_progress": "నా పురోగతి",
"track_learning_journey":
    "మీ అభ్యాస ప్రయాణం మరియు విజయాలను గమనించండి",

"completed": "పూర్తయింది",
                # =====================================================
        # PROFILE PAGE
        # =====================================================

        "profile_welcome":
            "మీ ప్రొఫైల్ మరియు అభ్యాస వివరాలను చూడండి.",

        "learner_profile":
            "అభ్యాసకుడి ప్రొఫైల్",

        "personal_information":
            "వ్యక్తిగత సమాచారం",

        "learning_statistics":
            "అభ్యాస గణాంకాలు",

        "learning_goal":
            "అభ్యాస లక్ష్యం",

        "learning_goal_description":
            "మీ అభ్యాస ప్రయాణాన్ని కొనసాగిస్తూ మీ నైపుణ్యాలను మెరుగుపరచుకోండి.",

        "beginner_journey":
            "ప్రారంభ అభ్యాస ప్రయాణం",

        "completed_percent":
            "పూర్తయింది",
                # Profile Page
        "profile_welcome":
            "View your profile and learning details.",

        "learner_profile":
            "Learner Profile",

        "personal_information":
            "Personal Information",

        "learning_statistics":
            "Learning Statistics",

        "learning_goal":
            "Learning Goal",

        "learning_goal_description":
            "Continue your learning journey and improve your skills.",

        "beginner_journey":
            "Beginner Learning Journey",

        "completed_percent":
            "completed",

        "learner":
            "Learner",


       
        "assessment": "ప్రాథమిక మూల్యాంకనం",
        "assessment_title": "ప్రాథమిక మూల్యాంకనం",
        "assessment_instruction":
            "మీ ప్రస్తుత అభ్యాస స్థాయిని తెలుసుకోవడానికి ప్రశ్నలకు సమాధానం ఇవ్వండి.",
        "submit_assessment": "మూల్యాంకనాన్ని సమర్పించండి",
        "assessment_result": "మూల్యాంకన ఫలితం",
        "your_score": "మీ స్కోర్",
        "proficiency_level": "నైపుణ్య స్థాయి",
        "beginner": "ప్రారంభ స్థాయి",
        "intermediate": "మధ్యస్థ స్థాయి",
        "advanced": "అధునాతన స్థాయి",
        "assessment_complete":
            "మూల్యాంకనం విజయవంతంగా పూర్తయింది!",
        "start_learning": "అభ్యాసాన్ని ప్రారంభించండి",

        "question": "ప్రశ్న",
        "of": "లో",
        "correct": "సరైన సమాధానం!",
        "incorrect": "తప్పు సమాధానం",
        "explanation": "వివరణ",
        "continue": "కొనసాగించండి",
        "lesson_complete": "పాఠం పూర్తయింది!",
        "excellent": "అద్భుతమైన పని!",
        "good_job": "మంచి పని! సాధన కొనసాగించండి.",
        "keep_practicing":
            "మెరుగుపడటానికి మళ్లీ సాధన చేయండి.",
        "score": "స్కోర్",
        "xp_earned": "సంపాదించిన XP",
        "back_to_learning": "అభ్యాసానికి తిరిగి వెళ్లండి",

        "footer":
            "నేర్చుకోండి • సాధన చేయండి • అభివృద్ధి చెందండి",
                    # =====================================================
        # PROGRESS PAGE
        # =====================================================

        "my_progress": "నా పురోగతి",

        "track_learning_journey":
            "మీ అభ్యాస ప్రయాణం మరియు విజయాలను గమనించండి",

        "overall": "మొత్తం",

        "excellent_progress": "అద్భుతమైన పురోగతి!",

        "excellent_progress_desc":
            "మీరు చాలా మంచి పురోగతిని సాధిస్తున్నారు. ఇదే విధంగా కొనసాగించండి!",

        "great_progress": "చాలా మంచి పురోగతి!",

        "great_progress_desc":
            "మీ అభ్యాసం మంచి దిశలో కొనసాగుతోంది. మరింత అభ్యాసం చేయండి!",

        "good_start": "మంచి ప్రారంభం!",

        "good_start_desc":
            "మీరు మంచి ప్రారంభం చేశారు. మీ అభ్యాసాన్ని కొనసాగించండి!",

        "start_learning_journey":
            "మీ అభ్యాస ప్రయాణాన్ని ప్రారంభించండి!",

        "start_learning_journey_desc":
            "మీ పురోగతిని ప్రారంభించడానికి మీ మొదటి పాఠాన్ని పూర్తి చేయండి.",

        "skills_progress": "నైపుణ్యాల పురోగతి",

        "reading_desc":
            "చదివే సామర్థ్యాన్ని మెరుగుపరచండి",

        "writing_desc":
            "రచనా నైపుణ్యాలను మెరుగుపరచండి",

        "speaking_desc":
            "మాట్లాడే నైపుణ్యాలను మెరుగుపరచండి",

        "in_progress": "కొనసాగుతోంది",

        "not_started": "ప్రారంభించలేదు",

        "complete": "పూర్తి",

        "reading_excellent":
            "అద్భుతం! మీ చదవడం నైపుణ్యం చాలా బాగుంది.",

        "reading_keep":
            "మంచిది! మీ చదవడం నైపుణ్యాన్ని మరింత అభ్యసించండి.",

        "reading_start":
            "చదవడం అభ్యాసాన్ని ప్రారంభించండి.",

        "writing_excellent":
            "అద్భుతం! మీ రాయడం నైపుణ్యం చాలా బాగుంది.",

        "writing_keep":
            "మంచిది! మీ రాయడం నైపుణ్యాన్ని మరింత అభ్యసించండి.",

        "writing_start":
            "రాయడం అభ్యాసాన్ని ప్రారంభించండి.",

        "speaking_excellent":
            "అద్భుతం! మీ మాట్లాడే నైపుణ్యం చాలా బాగుంది.",

        "speaking_keep":
            "మంచిది! మీ మాట్లాడే నైపుణ్యాన్ని మరింత అభ్యసించండి.",

        "speaking_start":
            "మాట్లాడే అభ్యాసాన్ని ప్రారంభించండి.",

        "recent_activity":
            "ఇటీవలి కార్యకలాపాలు",

        "lesson_completed":
            "పాఠం పూర్తయింది",

        "lesson_in_progress":
            "పాఠం కొనసాగుతోంది",

        "no_lessons_completed":
            "ఇంకా పాఠాలు పూర్తి చేయలేదు",

        "achievements":
            "విజయాలు",

        "first_lesson":
            "మొదటి పాఠం",

        "complete_first_lesson":
            "మీ మొదటి పాఠాన్ని పూర్తి చేయండి",

        "xp_builder":
            "XP బిల్డర్",

        "earn_learning_xp":
            "అభ్యాసం ద్వారా XP సంపాదించండి",

        "reading_star":
            "చదవడం స్టార్",

        "complete_reading_lessons":
            "చదవడం పాఠాలను పూర్తి చేయండి",

        "speaking_starter":
            "మాట్లాడటం ప్రారంభం",

        "practice_speaking":
            "మాట్లాడే అభ్యాసం చేయండి",

        "perfect_score":
            "పూర్తి స్కోర్",

        "get_100_score":
            "100% స్కోర్ సాధించండి",

        "keep_going_title":
            "కొనసాగించండి!",

        "every_lesson_goal":
            "ప్రతి పాఠం మీ లక్ష్యానికి ఒక అడుగు ముందుకు.",
            "learning_games": "అభ్యాస ఆటలు",
            "sentence_builder_game": "వాక్య నిర్మాణం",
"sentence_builder_description": "పదాలను సరైన క్రమంలో అమర్చి వాక్యాన్ని రూపొందించండి.",

"speed_spell_game": "వేగవంతమైన స్పెల్లింగ్",
"speed_spell_description": "సమయం ముగిసేలోపు పదాన్ని సరిగ్గా టైప్ చేయండి.",

"picture_match_game": "చిత్రం జోడింపు",
"picture_match_description": "చిత్రాన్ని సరైన పదంతో జోడించండి.",

"missing_word_game": "తప్పిపోయిన పదం",
"missing_word_description": "వాక్యాన్ని పూర్తి చేయడానికి సరైన పదాన్ని ఎంచుకోండి.",

"word_search_game": "పదాల శోధన",
"word_search_description": "గ్రిడ్‌లో సరైన అభ్యాస పదాన్ని కనుగొనండి.",

"picture_puzzle_game": "చిత్ర పజిల్",
"picture_puzzle_description": "చిత్రాన్ని చూసి పద భాగాలను సరైన క్రమంలో అమర్చండి.",
            
"practice_play": "అభ్యాసం & ఆట",
"word_match_game": "పదాల జోడింపు",
"word_match_description": "ప్రతి పదాన్ని సరైన అర్థంతో జోడించండి.",
"word_scramble_game": "పదాల అమరిక",
"word_scramble_description": "అక్షరాలను సరిగా అమర్చి సరైన పదాన్ని కనుగొనండి.",
"memory_match_game": "జ్ఞాపకశక్తి జోడింపు",
"memory_match_description": "చిత్రాలను సరైన పదాలతో జోడించండి.",
"listen_choose_game": "విని ఎంచుకోండి",
"listen_choose_description": "జాగ్రత్తగా విని సరైన పదాన్ని ఎంచుకోండి.",
"five_questions": "5 ప్రశ్నలు",
"five_rounds": "5 రౌండ్లు",
"start_game": "ఆట ప్రారంభించండి",
"question_of": "ప్రశ్న",
"round_of": "రౌండ్",
"score": "స్కోర్",
"correct_great_job": "✅ సరైన సమాధానం! చాలా బాగా చేశారు!",
"correct_match": "✅ సరైన జోడింపు! అద్భుతం!",
"correct_listening": "✅ సరైన వినికిడి సమాధానం!",
"not_quite": "❌ అది సరైన సమాధానం కాదు.",
"correct_answer": "సరైన సమాధానం",
"not_a_match": "❌ జోడింపు సరైంది కాదు. తదుపరి రౌండ్ ప్రయత్నించండి!",
"unscramble_word": "పదాన్ని సరిగా అమర్చండి",
"type_answer": "మీ సమాధానాన్ని నమోదు చేయండి",
"submit_answer": "సమాధానం పంపండి",
"find_matching_pair": "చిత్రాన్ని సరైన పదంతో జోడించండి",
"memory_instruction": "రెండు కార్డులను క్లిక్ చేసి సరైన జోడింపును కనుగొనండి.",
"listen_correct_word": "విని సరైన పదాన్ని ఎంచుకోండి",
"listen_again": "మళ్లీ వినండి",
"completed": "పూర్తయింది",
"success": "విజయం!",
"excellent_memory": "అద్భుతమైన జ్ఞాపకశక్తి!",
"keep_improving": "ఇంకా అభ్యాసం చేయండి!",
"play_again": "మళ్లీ ఆడండి",
"close_game": "ఆట మూసివేయండి",
"excellent_word_knowledge": "అద్భుతం! మీ పదాల పరిజ్ఞానం చాలా బాగుంది.",
"practice_words": "మంచి ప్రయత్నం! మీ పదాల నైపుణ్యాన్ని మెరుగుపరచడానికి మళ్లీ అభ్యాసం చేయండి.",
"excellent_scramble": "అద్భుతం! మీరు పదాలను చాలా బాగా అమర్చారు.",
"practice_spelling": "పదాల స్పెల్లింగ్‌ను అభ్యాసం చేసి మళ్లీ ప్రయత్నించండి.",
"excellent_memory_message": "అద్భుతం! మీ జ్ఞాపకశక్తి మరియు పదజ్ఞానం చాలా బాగా అభివృద్ధి చెందుతున్నాయి.",
"practice_memory": "చిత్రాలు మరియు పదాలను జోడించడం మరింత అభ్యాసం చేయండి.",
"excellent_listening": "అద్భుతమైన వినికిడి! మీరు పదాలను సరిగ్గా గుర్తించారు.",
"practice_listening": "జాగ్రత్తగా విని మీ వినికిడి నైపుణ్యాన్ని మెరుగుపరచడానికి మళ్లీ ప్రయత్నించండి.",
"please_enter_answer": "దయచేసి సమాధానాన్ని నమోదు చేయండి.",
"learning_games": "అభ్యాస ఆటలు",
"practice_play": "అభ్యాసం & ఆట",
"word_match_game": "పదాల జోడింపు",
"word_match_description": "ప్రతి పదాన్ని సరైన అర్థంతో జోడించండి.",
"word_scramble_game": "పదాల అమరిక",
"word_scramble_description": "అక్షరాలను సరిగా అమర్చి సరైన పదాన్ని కనుగొనండి.",
"memory_match_game": "జ్ఞాపకశక్తి జోడింపు",
"memory_match_description": "చిత్రాలను సరైన పదాలతో జోడించండి.",
"listen_choose_game": "విని ఎంచుకోండి",
"listen_choose_description": "జాగ్రత్తగా విని సరైన పదాన్ని ఎంచుకోండి.",
"five_questions": "5 ప్రశ్నలు",
"five_rounds": "5 రౌండ్లు",
"start_game": "ఆట ప్రారంభించండి",
"unscramble_word": "పదాన్ని సరిగా అమర్చండి",
"find_matching_pair": "చిత్రాన్ని సరైన పదంతో జోడించండి",
"memory_instruction": "రెండు కార్డులను క్లిక్ చేసి సరైన జోడింపును కనుగొనండి.",
"listen_correct_word": "విని సరైన పదాన్ని ఎంచుకోండి",
"listen_again": "మళ్లీ వినండి",
"submit_answer": "సమాధానం పంపండి",
"play_again": "మళ్లీ ఆడండి",
"close_game": "ఆట మూసివేయండి",
"success": "విజయం!",
"keep_improving": "ఇంకా అభ్యాసం చేయండి!",

        
            
    },



    # =====================================================
    # HINDI
    # =====================================================

    "Hindi": {

        "home": "होम",
        "dashboard": "डैशबोर्ड",
        "learn": "सीखें",
        "voice": "आवाज़",
        "progress": "प्रगति",
        "profile": "प्रोफ़ाइल",
        "logout": "लॉग आउट",
        "register": "पंजीकरण",
        "login": "लॉगिन",

        "welcome": "IntelliLearn में आपका स्वागत है",
        "welcome_back": "वापसी पर स्वागत है",
        "ready":
            "क्या आप अपनी सीखने की यात्रा जारी रखने के लिए तैयार हैं?",

        "learning_progress": "सीखने की प्रगति",
        "overall_progress": "कुल प्रगति",
        "reading_progress": "पढ़ने की प्रगति",
        "writing_progress": "लिखने की प्रगति",
        "speaking_progress": "बोलने की प्रगति",
        "keep_going":
            "जारी रखें! आप बहुत अच्छा कर रहे हैं।",

        "learning_path": "आपका सीखने का मार्ग",
        "complete_lessons":
            "अपने कौशल को बेहतर बनाने के लिए पाठ पूरे करें।",

        "reading": "पढ़ना",
        "writing": "लिखना",
        "speaking": "बोलना",

        "alphabet": "वर्णमाला",
        "alphabet_basics": "वर्णमाला की मूल बातें",
        "alphabet_description":
            "मूल अक्षरों और उनकी ध्वनियों को सीखें।",

        "basic_words": "मूल शब्द",
        "basic_words_description":
            "रोज़मर्रा में उपयोग होने वाले सामान्य शब्द सीखें।",

        "sentences": "वाक्य",
        "simple_sentences": "सरल वाक्य",
        "simple_sentences_description":
            "सरल वाक्यों को पढ़ने और समझने का अभ्यास करें।",

        "choose_lesson": "पाठ चुनें",
        "lesson_label": "पाठ",
        "practice": "अभ्यास",
        "daily_challenge": "दैनिक सीखने की चुनौती",
        "daily_challenge_description": "आज का आकलन पूरा करें और XP अर्जित करके अपना स्तर सुधारें।",
        "beginner_level": "शुरुआती स्तर",

        "start": "शुरू करें",
        "continue_learning": "सीखना जारी रखें",
        "next": "अगला",
        "back": "वापस",
        "submit": "जमा करें",
        "save": "सहेजें",

        "day_streak": "दिनों की स्ट्रीक",
        "total_xp": "कुल XP",
        "current_level": "वर्तमान स्तर",

        "voice_practice": "आवाज़ का अभ्यास",
        "start_speaking": "बोलना शुरू करें",
        "voice_title": "बोलने का अभ्यास",
        "voice_instruction":
            "वाक्य सुनें और उसे स्पष्ट रूप से दोहराएँ।",
        "voice_sentence": "अभ्यास वाक्य",
        "listen": "सुनें",
        "stop_speaking": "बोलना बंद करें",
        "voice_ready": "सुनने के लिए तैयार",
        "voice_listening": "सुन रहा है...",
        "voice_result":
            "आपकी आवाज़ रिकॉर्ड हो गई है।",

        "choose_skill": "कौशल चुनें",
        "my_profile": "मेरी प्रोफ़ाइल",
        "edit_profile": "प्रोफ़ाइल संपादित करें",
        "full_name": "पूरा नाम",
        "email": "ईमेल",
        "password": "पासवर्ड",
        "preferred_language": "पसंदीदा भाषा",
        "learning_language": "सीखने की भाषा",

                # Profile Page
        "profile_welcome":
            "अपनी प्रोफ़ाइल और सीखने का विवरण देखें।",

        "learner_profile":
            "शिक्षार्थी प्रोफ़ाइल",

        "personal_information":
            "व्यक्तिगत जानकारी",

        "learning_statistics":
            "सीखने के आँकड़े",

        "learning_goal":
            "सीखने का लक्ष्य",

        "learning_goal_description":
            "अपनी सीखने की यात्रा जारी रखें और अपने कौशल में सुधार करें।",

        "beginner_journey":
            "शुरुआती सीखने की यात्रा",

        "completed_percent":
            "पूरा हुआ",

        "learner":
            "शिक्षार्थी",

        "progress_title": "मेरी प्रगति",
        "progress_subtitle":
            "अपनी सीखने की यात्रा को ट्रैक करें।",
        "completed": "पूरा हुआ",

        "assessment": "प्रारंभिक मूल्यांकन",
        "assessment_title": "प्रारंभिक मूल्यांकन",
        "assessment_instruction":
            "अपने वर्तमान सीखने के स्तर को समझने के लिए प्रश्नों के उत्तर दें।",
        "submit_assessment": "मूल्यांकन जमा करें",
        "assessment_result": "मूल्यांकन परिणाम",
        "your_score": "आपका स्कोर",
        "proficiency_level": "दक्षता स्तर",
        "beginner": "शुरुआती",
        "intermediate": "मध्यवर्ती",
        "advanced": "उन्नत",
        "assessment_complete":
            "मूल्यांकन सफलतापूर्वक पूरा हुआ!",
        "start_learning": "सीखना शुरू करें",

        "question": "प्रश्न",
        "of": "में से",
        "correct": "सही उत्तर!",
        "incorrect": "गलत उत्तर",
        "explanation": "व्याख्या",
        "continue": "जारी रखें",
        "lesson_complete": "पाठ पूरा हुआ!",
        "excellent": "बहुत बढ़िया!",
        "good_job": "अच्छा काम! अभ्यास जारी रखें।",
        "keep_practicing":
            "सुधार करने के लिए फिर से अभ्यास करें।",
        "score": "स्कोर",
        "xp_earned": "प्राप्त XP",
        "back_to_learning": "सीखने पर वापस जाएँ",
        "learning_games": "सीखने के खेल",
        "sentence_builder_game": "वाक्य निर्माण",
"sentence_builder_description": "शब्दों को सही क्रम में लगाकर वाक्य बनाएँ।",

"speed_spell_game": "तेज़ वर्तनी",
"speed_spell_description": "समय समाप्त होने से पहले शब्द सही लिखें।",

"picture_match_game": "चित्र मिलान",
"picture_match_description": "चित्र को सही शब्द से मिलाएँ।",

"missing_word_game": "लापता शब्द",
"missing_word_description": "वाक्य पूरा करने के लिए सही शब्द चुनें।",

"word_search_game": "शब्द खोज",
"word_search_description": "ग्रिड में सही सीखने वाला शब्द खोजें।",

"picture_puzzle_game": "चित्र पहेली",
"picture_puzzle_description": "चित्र देखें और शब्द के टुकड़ों को सही क्रम में लगाएँ।",
"practice_play": "अभ्यास और खेल",
"word_match_game": "शब्द मिलान",
"word_match_description": "हर शब्द को उसके सही अर्थ से मिलाएँ।",
"word_scramble_game": "शब्द क्रम",
"word_scramble_description": "अक्षरों को सही क्रम में लगाकर शब्द बनाएँ।",
"memory_match_game": "स्मृति मिलान",
"memory_match_description": "चित्रों को उनके सही शब्दों से मिलाएँ।",
"listen_choose_game": "सुनें और चुनें",
"listen_choose_description": "ध्यान से सुनें और सही शब्द चुनें।",
"five_questions": "5 प्रश्न",
"five_rounds": "5 राउंड",
"start_game": "खेल शुरू करें",
"question_of": "प्रश्न",
"round_of": "राउंड",
"score": "स्कोर",
"correct_great_job": "✅ सही! बहुत अच्छा!",
"correct_match": "✅ सही मिलान! शानदार!",
"correct_listening": "✅ सही सुनने का उत्तर!",
"not_quite": "❌ सही नहीं।",
"correct_answer": "सही उत्तर",
"not_a_match": "❌ मिलान सही नहीं है। अगला राउंड आज़माएँ!",
"unscramble_word": "शब्द को सही क्रम में लगाएँ",
"type_answer": "अपना उत्तर लिखें",
"submit_answer": "उत्तर जमा करें",
"find_matching_pair": "चित्र को सही शब्द से मिलाएँ",
"memory_instruction": "दो कार्डों पर क्लिक करके सही जोड़ी खोजें।",
"listen_correct_word": "सुनें और सही शब्द चुनें",
"listen_again": "फिर से सुनें",
"completed": "पूरा हुआ",
"success": "सफलता!",
"excellent_memory": "उत्कृष्ट स्मृति!",
"keep_improving": "अभ्यास जारी रखें!",
"play_again": "फिर से खेलें",
"close_game": "खेल बंद करें",
"excellent_word_knowledge": "बहुत बढ़िया! आपके शब्द ज्ञान की क्षमता अच्छी है।",
"practice_words": "अच्छा प्रयास! अपने शब्द कौशल को बेहतर करने के लिए फिर से अभ्यास करें।",
"excellent_scramble": "शानदार! आपने शब्दों को बहुत अच्छी तरह हल किया।",
"practice_spelling": "वर्तनी का अभ्यास करें और फिर से प्रयास करें।",
"excellent_memory_message": "बहुत बढ़िया! आपकी स्मृति और शब्दावली कौशल अच्छी तरह विकसित हो रहे हैं।",
"practice_memory": "चित्रों और शब्दों का मिलान करके अधिक अभ्यास करें।",
"excellent_listening": "उत्कृष्ट सुनने का कौशल! आपने शब्दों को सही पहचाना।",
"practice_listening": "ध्यान से सुनें और अपनी सुनने की क्षमता सुधारने के लिए फिर से अभ्यास करें।",
"please_enter_answer": "कृपया उत्तर दर्ज करें।",
"learning_games": "सीखने के खेल",
"practice_play": "अभ्यास और खेल",
"word_match_game": "शब्द मिलान",
"word_match_description": "हर शब्द को उसके सही अर्थ से मिलाएँ।",
"word_scramble_game": "शब्द क्रम",
"word_scramble_description": "अक्षरों को सही क्रम में लगाकर शब्द बनाएँ।",
"memory_match_game": "स्मृति मिलान",
"memory_match_description": "चित्रों को उनके सही शब्दों से मिलाएँ।",
"listen_choose_game": "सुनें और चुनें",
"listen_choose_description": "ध्यान से सुनें और सही शब्द चुनें।",
"five_questions": "5 प्रश्न",
"five_rounds": "5 राउंड",
"start_game": "खेल शुरू करें",
"unscramble_word": "शब्द को सही क्रम में लगाएँ",
"find_matching_pair": "चित्र को सही शब्द से मिलाएँ",
"memory_instruction": "दो कार्डों पर क्लिक करके सही जोड़ी खोजें।",
"listen_correct_word": "सुनें और सही शब्द चुनें",
"listen_again": "फिर से सुनें",
"submit_answer": "उत्तर जमा करें",
"play_again": "फिर से खेलें",
"close_game": "खेल बंद करें",
"success": "सफलता!",
"keep_improving": "अभ्यास जारी रखें!",

        "footer":
            "सीखें • अभ्यास करें • सुधारें"
    }
}


# =========================================================
# LOCALIZED LESSON DISPLAY
# =========================================================
# The LESSONS dictionary contains the original lesson data used
# internally for scoring.  This function creates a display copy
# so the lesson list/title/description follows the user's
# PREFERRED language without changing the answer-checking data.
# =========================================================
# =========================================================
# MULTILINGUAL CONTENT REPOSITORY
# =========================================================
# This repository stores lesson titles and descriptions
# in the learner's preferred language.
#
# Supported languages:
# English
# Telugu
# Hindi
# =========================================================

LESSON_DISPLAY_TRANSLATIONS = {

    # =====================================================
    # ENGLISH
    # =====================================================

    "English": {

        "alphabet": {
            "title": "Alphabet",
            "description":
                "Learn and recognize English letters from A to Z."
        },

        "sounds": {
            "title": "Letter Sounds",
            "description":
                "Learn the sounds of common English letters."
        },

        "alphabet_examples": {
            "title": "Alphabet Examples",
            "description":
                "Learn words that begin with different letters."
        },

        "basic_words": {
            "title": "Basic Words",
            "description":
                "Learn common English words used every day."
        },

        "family_words": {
            "title": "Family Words",
            "description":
                "Learn common words used for family members."
        },

        "food_words": {
            "title": "Food Words",
            "description":
                "Learn common words related to food and drinks."
        },

        "colors": {
            "title": "Colors",
            "description":
                "Learn the names of common colors."
        },

        "numbers": {
            "title": "Numbers",
            "description":
                "Learn to recognize and use basic numbers."
        },

        "animals": {
            "title": "Animals",
            "description":
                "Learn the names of common animals."
        },

        "simple_sentences": {
            "title": "Simple Sentences",
            "description":
                "Practice reading and understanding simple sentences."
        }
    },


    # =====================================================
    # TELUGU
    # =====================================================

    "Telugu": {

        "alphabet": {
            "title": "అక్షరమాల",
            "description":
                "A నుండి Z వరకు ఇంగ్లీష్ అక్షరాలను గుర్తించడం మరియు నేర్చుకోవడం."
        },

        "sounds": {
            "title": "అక్షరాల ధ్వనులు",
            "description":
                "సాధారణ ఇంగ్లీష్ అక్షరాల ధ్వనులను నేర్చుకోండి."
        },

        "alphabet_examples": {
            "title": "అక్షరాల ఉదాహరణలు",
            "description":
                "వివిధ అక్షరాలతో ప్రారంభమయ్యే పదాలను నేర్చుకోండి."
        },

        "basic_words": {
            "title": "ప్రాథమిక పదాలు",
            "description":
                "ప్రతిరోజూ ఉపయోగించే సాధారణ ఇంగ్లీష్ పదాలను నేర్చుకోండి."
        },

        "family_words": {
            "title": "కుటుంబ పదాలు",
            "description":
                "కుటుంబ సభ్యులను సూచించే సాధారణ పదాలను నేర్చుకోండి."
        },

        "food_words": {
            "title": "ఆహార పదాలు",
            "description":
                "ఆహారం మరియు పానీయాలకు సంబంధించిన సాధారణ పదాలను నేర్చుకోండి."
        },

        "colors": {
            "title": "రంగులు",
            "description":
                "వివిధ సాధారణ రంగుల పేర్లను నేర్చుకోండి."
        },

        "numbers": {
            "title": "సంఖ్యలు",
            "description":
                "ప్రాథమిక సంఖ్యలను గుర్తించడం మరియు ఉపయోగించడం నేర్చుకోండి."
        },

        "animals": {
            "title": "జంతువులు",
            "description":
                "సాధారణ జంతువుల పేర్లను నేర్చుకోండి."
        },

        "simple_sentences": {
            "title": "సరళమైన వాక్యాలు",
            "description":
                "సరళమైన వాక్యాలను చదవడం మరియు అర్థం చేసుకోవడం అభ్యసించండి."
        }
    },


    # =====================================================
    # HINDI
    # =====================================================

    "Hindi": {

        "alphabet": {
            "title": "वर्णमाला",
            "description":
                "A से Z तक अंग्रेज़ी अक्षरों को पहचानना और सीखना।"
        },

        "sounds": {
            "title": "अक्षरों की ध्वनियाँ",
            "description":
                "सामान्य अंग्रेज़ी अक्षरों की ध्वनियाँ सीखें।"
        },

        "alphabet_examples": {
            "title": "वर्णमाला के उदाहरण",
            "description":
                "अलग-अलग अक्षरों से शुरू होने वाले शब्द सीखें।"
        },

        "basic_words": {
            "title": "मूल शब्द",
            "description":
                "रोज़मर्रा में उपयोग होने वाले सामान्य अंग्रेज़ी शब्द सीखें।"
        },

        "family_words": {
            "title": "परिवार के शब्द",
            "description":
                "परिवार के सदस्यों के लिए उपयोग होने वाले सामान्य शब्द सीखें।"
        },

        "food_words": {
            "title": "भोजन के शब्द",
            "description":
                "भोजन और पेय से जुड़े सामान्य शब्द सीखें।"
        },

        "colors": {
            "title": "रंग",
            "description":
                "विभिन्न सामान्य रंगों के नाम सीखें।"
        },

        "numbers": {
            "title": "संख्याएँ",
            "description":
                "मूल संख्याओं को पहचानना और उपयोग करना सीखें।"
        },

        "animals": {
            "title": "जानवर",
            "description":
                "सामान्य जानवरों के नाम सीखें।"
        },

        "simple_sentences": {
            "title": "सरल वाक्य",
            "description":
                "सरल वाक्यों को पढ़ने और समझने का अभ्यास करें।"
        }
    }
}
# =========================================================
# LEARNING CONTENT TRANSLATIONS
# =========================================================
# These translations are for the actual lesson questions,
# options and explanations.
#
# IMPORTANT:
# These follow the LEARNING LANGUAGE, not the
# Preferred Language.
# =========================================================

LESSON_CONTENT_TRANSLATIONS = {

    "Telugu": {

        "alphabet": {
            "questions": [
                {
                    "question": "A తర్వాత ఏ అక్షరం వస్తుంది?",
                    "options": ["B", "C", "D", "E"],
                    "answer": "B",
                    "help": "A తర్వాత B వస్తుంది."
                },
                {
                    "question": "D ముందు ఏ అక్షరం వస్తుంది?",
                    "options": ["A", "B", "C", "E"],
                    "answer": "C",
                    "help": "అక్షరాల క్రమం A, B, C, D."
                },
                {
                    "question": "ఆంగ్ల అక్షరమాలలో మొదటి అక్షరం ఏది?",
                    "options": ["A", "B", "C", "D"],
                    "answer": "A",
                    "help": "ఆంగ్ల అక్షరమాల A తో ప్రారంభమవుతుంది."
                }
            ]
        },

        "basic_words": {
            "questions": [
                {
                    "question": "క్రిందివాటిలో 'నీరు' అనే పదానికి ఆంగ్ల పదం ఏది?",
                    "options": ["Water", "Food", "Book", "House"],
                    "answer": "Water",
                    "help": "నీరు = Water."
                },
                {
                    "question": "క్రిందివాటిలో 'పుస్తకం' అనే పదానికి ఆంగ్ల పదం ఏది?",
                    "options": ["Book", "Pen", "Chair", "Table"],
                    "answer": "Book",
                    "help": "పుస్తకం = Book."
                }
            ]
        },

        "family_words": {
            "questions": [
                {
                    "question": "'తల్లి' అనే పదానికి ఆంగ్ల పదం ఏది?",
                    "options": ["Mother", "Father", "Brother", "Sister"],
                    "answer": "Mother",
                    "help": "తల్లి = Mother."
                },
                {
                    "question": "'తండ్రి' అనే పదానికి ఆంగ్ల పదం ఏది?",
                    "options": ["Mother", "Father", "Sister", "Daughter"],
                    "answer": "Father",
                    "help": "తండ్రి = Father."
                }
            ]
        },

        "food_words": {
            "questions": [
                {
                    "question": "'ఆపిల్' అనే పదానికి ఆంగ్ల పదం ఏది?",
                    "options": ["Apple", "Rice", "Milk", "Bread"],
                    "answer": "Apple",
                    "help": "ఆపిల్ = Apple."
                },
                {
                    "question": "'పాలు' అనే పదానికి ఆంగ్ల పదం ఏది?",
                    "options": ["Milk", "Water", "Juice", "Tea"],
                    "answer": "Milk",
                    "help": "పాలు = Milk."
                }
            ]
        },

        "colors": {
            "questions": [
                {
                    "question": "'ఎరుపు' అనే రంగుకు ఆంగ్ల పదం ఏది?",
                    "options": ["Red", "Blue", "Green", "Yellow"],
                    "answer": "Red",
                    "help": "ఎరుపు = Red."
                },
                {
                    "question": "'నీలం' అనే రంగుకు ఆంగ్ల పదం ఏది?",
                    "options": ["Blue", "Red", "Black", "White"],
                    "answer": "Blue",
                    "help": "నీలం = Blue."
                }
            ]
        },

        "numbers": {
            "questions": [
                {
                    "question": "ఒకటి అనే సంఖ్యకు ఆంగ్ల పదం ఏది?",
                    "options": ["One", "Two", "Three", "Four"],
                    "answer": "One",
                    "help": "ఒకటి = One."
                },
                {
                    "question": "రెండు అనే సంఖ్యకు ఆంగ్ల పదం ఏది?",
                    "options": ["One", "Two", "Three", "Five"],
                    "answer": "Two",
                    "help": "రెండు = Two."
                }
            ]
        },

        "animals": {
            "questions": [
                {
                    "question": "'కుక్క' అనే పదానికి ఆంగ్ల పదం ఏది?",
                    "options": ["Dog", "Cat", "Cow", "Horse"],
                    "answer": "Dog",
                    "help": "కుక్క = Dog."
                },
                {
                    "question": "'పిల్లి' అనే పదానికి ఆంగ్ల పదం ఏది?",
                    "options": ["Cat", "Dog", "Bird", "Fish"],
                    "answer": "Cat",
                    "help": "పిల్లి = Cat."
                }
            ]
        },

        "simple_sentences": {
            "questions": [
                {
                    "question": "'నేను విద్యార్థిని' అనే వాక్యానికి సరైన ఆంగ్ల వాక్యం ఏది?",
                    "options": [
                        "I am a student.",
                        "I am a teacher.",
                        "You are a student.",
                        "He is a student."
                    ],
                    "answer": "I am a student.",
                    "help": "నేను విద్యార్థిని = I am a student."
                }
            ]
        }
    },


    # =====================================================
    # HINDI
    # =====================================================

    "Hindi": {

        "alphabet": {
            "questions": [
                {
                    "question": "A के बाद कौन सा अक्षर आता है?",
                    "options": ["B", "C", "D", "E"],
                    "answer": "B",
                    "help": "A के बाद B आता है।"
                },
                {
                    "question": "D से पहले कौन सा अक्षर आता है?",
                    "options": ["A", "B", "C", "E"],
                    "answer": "C",
                    "help": "क्रम A, B, C, D है।"
                },
                {
                    "question": "अंग्रेज़ी वर्णमाला का पहला अक्षर कौन सा है?",
                    "options": ["A", "B", "C", "D"],
                    "answer": "A",
                    "help": "अंग्रेज़ी वर्णमाला A से शुरू होती है।"
                }
            ]
        },

        "basic_words": {
            "questions": [
                {
                    "question": "'पानी' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Water", "Food", "Book", "House"],
                    "answer": "Water",
                    "help": "पानी = Water."
                },
                {
                    "question": "'किताब' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Book", "Pen", "Chair", "Table"],
                    "answer": "Book",
                    "help": "किताब = Book."
                }
            ]
        },

        "family_words": {
            "questions": [
                {
                    "question": "'माँ' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Mother", "Father", "Brother", "Sister"],
                    "answer": "Mother",
                    "help": "माँ = Mother."
                },
                {
                    "question": "'पिता' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Mother", "Father", "Sister", "Daughter"],
                    "answer": "Father",
                    "help": "पिता = Father."
                }
            ]
        },

        "food_words": {
            "questions": [
                {
                    "question": "'सेब' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Apple", "Rice", "Milk", "Bread"],
                    "answer": "Apple",
                    "help": "सेब = Apple."
                },
                {
                    "question": "'दूध' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Milk", "Water", "Juice", "Tea"],
                    "answer": "Milk",
                    "help": "दूध = Milk."
                }
            ]
        },

        "colors": {
            "questions": [
                {
                    "question": "'लाल' रंग का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Red", "Blue", "Green", "Yellow"],
                    "answer": "Red",
                    "help": "लाल = Red."
                },
                {
                    "question": "'नीला' रंग का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Blue", "Red", "Black", "White"],
                    "answer": "Blue",
                    "help": "नीला = Blue."
                }
            ]
        },

        "numbers": {
            "questions": [
                {
                    "question": "'एक' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["One", "Two", "Three", "Four"],
                    "answer": "One",
                    "help": "एक = One."
                },
                {
                    "question": "'दो' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["One", "Two", "Three", "Five"],
                    "answer": "Two",
                    "help": "दो = Two."
                }
            ]
        },

        "animals": {
            "questions": [
                {
                    "question": "'कुत्ता' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Dog", "Cat", "Cow", "Horse"],
                    "answer": "Dog",
                    "help": "कुत्ता = Dog."
                },
                {
                    "question": "'बिल्ली' का अंग्रेज़ी शब्द क्या है?",
                    "options": ["Cat", "Dog", "Bird", "Fish"],
                    "answer": "Cat",
                    "help": "बिल्ली = Cat."
                }
            ]
        },

        "simple_sentences": {
            "questions": [
                {
                    "question": "'मैं एक विद्यार्थी हूँ' का सही अंग्रेज़ी वाक्य कौन सा है?",
                    "options": [
                        "I am a student.",
                        "I am a teacher.",
                        "You are a student.",
                        "He is a student."
                    ],
                    "answer": "I am a student.",
                    "help": "मैं एक विद्यार्थी हूँ = I am a student."
                }
            ]
        }
    }
}
def get_localized_lessons():
    """
    Return lessons using the learner's LEARNING LANGUAGE.

    Preferred Language:
        UI / navigation / dashboard

    Learning Language:
        Actual lesson content
    """

    learning_language = get_learning_language()

    display_translations = LESSON_DISPLAY_TRANSLATIONS.get(
        learning_language,
        {}
    )

    content_translations = LESSON_CONTENT_TRANSLATIONS.get(
        learning_language,
        {}
    )

    localized_lessons = {}

    for lesson_name, lesson in LESSONS.items():

        localized_lesson = dict(lesson)

        # -------------------------------------------------
        # TITLE + DESCRIPTION
        # -------------------------------------------------

        lesson_translation = display_translations.get(
            lesson_name,
            {}
        )

        if lesson_translation.get("title"):
            localized_lesson["title"] = (
                lesson_translation["title"]
            )

        if lesson_translation.get("description"):
            localized_lesson["description"] = (
                lesson_translation["description"]
            )

        # -------------------------------------------------
        # QUESTIONS
        # -------------------------------------------------

        original_questions = lesson.get(
            "questions",
            []
        )

        translated_content = content_translations.get(
            lesson_name,
            {}
        )

        translated_questions = translated_content.get(
            "questions",
            []
        )

        if translated_questions:

            localized_lesson["questions"] = (
                translated_questions
            )

        else:

            # If translation does not exist,
            # keep original English questions.
            localized_lesson["questions"] = [
                dict(q)
                for q in original_questions
            ]

        localized_lessons[lesson_name] = localized_lesson

    return localized_lessons
def get_current_language():

    if "user_id" not in session:
        return "English"


    # First use the language stored in the current session

    if "preferred_language" in session:

        language = session["preferred_language"]

        if language in TRANSLATIONS:
            return language


    # Otherwise get the language from database

    try:

        connection = get_db_connection()

        user = connection.execute(
            """
            SELECT preferred_language
            FROM users
            WHERE id = ?
            """,
            (session["user_id"],)
        ).fetchone()

        connection.close()


        if user and user["preferred_language"]:

            language = user["preferred_language"].strip()

            if language in TRANSLATIONS:
                return language


    except Exception as e:

        print("Preferred language error:", e)


    return "English"

# =========================================================
# GET LEARNING LANGUAGE
# =========================================================
def get_learning_language():

    if "user_id" not in session:
        return "English"

    try:
        connection = get_db_connection()

        user = connection.execute(
            """
            SELECT learning_language
            FROM users
            WHERE id = ?
            """,
            (session["user_id"],)
        ).fetchone()

        connection.close()

        if user and user["learning_language"]:

            language = user["learning_language"].strip()

            return language

    except Exception as e:
        print("Learning language error:", e)

    return "English"

def get_learning_game_data(): 
 
    learning_language = get_learning_language()
# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_db_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


# =========================================================
# LANGUAGE FUNCTIONS
# =========================================================


def translate(key):
    """
    Translate interface text using the user's
    PREFERRED LANGUAGE.

    This function is ONLY for UI text.
    Lessons use the LEARNING LANGUAGE separately.
    """

    language = get_current_language()

    if language not in TRANSLATIONS:
        language = "English"

    return TRANSLATIONS[language].get(
        key,
        TRANSLATIONS["English"].get(key, key)
    )

@app.context_processor
def inject_language():

    preferred_language = get_current_language()

    learning_language = get_learning_language()

    return {
        "t": translate,
        "current_language": preferred_language,
        "preferred_language": preferred_language,
        "learning_language": learning_language
    }

# =========================================================
# DATABASE BACKUP
# =========================================================

def backup_database():

    if not os.path.exists(DATABASE):
        return

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    backup_name = (
        f"database_backup_{timestamp}.db"
    )

    try:

        shutil.copy2(
            DATABASE,
            backup_name
        )

        print(
            f"Database backup created: {backup_name}"
        )

    except Exception as e:

        print(
            "Could not create database backup:",
            e
        )


# =========================================================
# LESSON DATA
# IMPORTANT:
# THIS MUST COME BEFORE THE LESSON ROUTE
# =========================================================
LESSONS = {

    # =====================================================
    # 1. ALPHABET
    # =====================================================
    "alphabet": {
        "title": "Alphabet",
        "icon": "🔤",
        "description": "Learn and recognize English letters from A to Z.",
        "questions": [
            {
                "question": "Which letter comes after A?",
                "options": ["B", "C", "D", "E"],
                "answer": "B",
                "help": "B comes after A."
            },
            {
                "question": "Which letter comes before D?",
                "options": ["A", "B", "C", "E"],
                "answer": "C",
                "help": "The order is A, B, C, D."
            },
            {
                "question": "Which is the first letter of the alphabet?",
                "options": ["A", "B", "C", "D"],
                "answer": "A",
                "help": "The alphabet starts with A."
            },
            {
                "question": "Which letter comes after M?",
                "options": ["L", "N", "O", "P"],
                "answer": "N",
                "help": "N comes after M."
            },
            {
                "question": "Which letter comes before Z?",
                "options": ["X", "Y", "W", "V"],
                "answer": "Y",
                "help": "Y comes before Z."
            },
            {
                "question": "Which letter is between D and F?",
                "options": ["C", "E", "G", "H"],
                "answer": "E",
                "help": "D, E, F are in order."
            },
            {
                "question": "Which is the last letter of the alphabet?",
                "options": ["X", "Y", "Z", "W"],
                "answer": "Z",
                "help": "Z is the last letter."
            },
            {
                "question": "Which letter comes after S?",
                "options": ["R", "T", "U", "V"],
                "answer": "T",
                "help": "T comes after S."
            },
            {
                "question": "Which letter comes before P?",
                "options": ["O", "Q", "R", "N"],
                "answer": "O",
                "help": "O comes before P."
            },
            {
                "question": "Which of these is a vowel?",
                "options": ["B", "C", "A", "D"],
                "answer": "A",
                "help": "A is a vowel."
            }
        ]
    },


    # =====================================================
    # 2. LETTER SOUNDS
    # =====================================================
    "sounds": {
        "title": "Letter Sounds",
        "icon": "🔊",
        "description": "Learn the sounds of common English letters.",
        "questions": [
            {
                "question": "Which letter starts the word 'ball'?",
                "options": ["A", "B", "C", "D"],
                "answer": "B",
                "help": "Ball starts with B."
            },
            {
                "question": "Which letter starts the word 'cat'?",
                "options": ["A", "B", "C", "D"],
                "answer": "C",
                "help": "Cat starts with C."
            },
            {
                "question": "Which letter starts the word 'dog'?",
                "options": ["B", "C", "D", "E"],
                "answer": "D",
                "help": "Dog starts with D."
            },
            {
                "question": "Which letter starts the word 'fish'?",
                "options": ["F", "G", "H", "I"],
                "answer": "F",
                "help": "Fish starts with F."
            },
            {
                "question": "Which letter starts the word 'goat'?",
                "options": ["F", "G", "H", "I"],
                "answer": "G",
                "help": "Goat starts with G."
            },
            {
                "question": "Which letter starts the word 'hat'?",
                "options": ["G", "H", "I", "J"],
                "answer": "H",
                "help": "Hat starts with H."
            },
            {
                "question": "Which letter starts the word 'pen'?",
                "options": ["O", "P", "Q", "R"],
                "answer": "P",
                "help": "Pen starts with P."
            },
            {
                "question": "Which letter starts the word 'sun'?",
                "options": ["R", "S", "T", "U"],
                "answer": "S",
                "help": "Sun starts with S."
            },
            {
                "question": "Which letter starts the word 'van'?",
                "options": ["U", "V", "W", "X"],
                "answer": "V",
                "help": "Van starts with V."
            },
            {
                "question": "Which letter starts the word 'zebra'?",
                "options": ["W", "X", "Y", "Z"],
                "answer": "Z",
                "help": "Zebra starts with Z."
            }
        ]
    },


    # =====================================================
    # 3. ALPHABET EXAMPLES
    # =====================================================
    "alphabet_examples": {
        "title": "Alphabet Examples",
        "icon": "🅰️",
        "description": "Learn words that begin with different letters.",
        "questions": [
            {
                "question": "Which word begins with A?",
                "options": ["Apple", "Ball", "Cat", "Dog"],
                "answer": "Apple",
                "help": "Apple begins with A."
            },
            {
                "question": "Which word begins with B?",
                "options": ["Cat", "Ball", "Egg", "Fish"],
                "answer": "Ball",
                "help": "Ball begins with B."
            },
            {
                "question": "Which word begins with C?",
                "options": ["Dog", "Cat", "Fish", "Goat"],
                "answer": "Cat",
                "help": "Cat begins with C."
            },
            {
                "question": "Which word begins with D?",
                "options": ["Apple", "Dog", "Egg", "Hat"],
                "answer": "Dog",
                "help": "Dog begins with D."
            },
            {
                "question": "Which word begins with E?",
                "options": ["Egg", "Fish", "Goat", "Pen"],
                "answer": "Egg",
                "help": "Egg begins with E."
            },
            {
                "question": "Which word begins with F?",
                "options": ["Fish", "Goat", "Hat", "Sun"],
                "answer": "Fish",
                "help": "Fish begins with F."
            },
            {
                "question": "Which word begins with G?",
                "options": ["Hat", "Goat", "Pen", "Van"],
                "answer": "Goat",
                "help": "Goat begins with G."
            },
            {
                "question": "Which word begins with H?",
                "options": ["Hat", "Cat", "Dog", "Fish"],
                "answer": "Hat",
                "help": "Hat begins with H."
            },
            {
                "question": "Which word begins with P?",
                "options": ["Pen", "Sun", "Van", "Zebra"],
                "answer": "Pen",
                "help": "Pen begins with P."
            },
            {
                "question": "Which word begins with S?",
                "options": ["Van", "Sun", "Goat", "Apple"],
                "answer": "Sun",
                "help": "Sun begins with S."
            }
        ]
    },


    # =====================================================
    # 4. BASIC WORDS
    # =====================================================
    "basic_words": {
        "title": "Basic Words",
        "icon": "📖",
        "description": "Learn common English words used every day.",
        "questions": [
            {
                "question": "What do we read?",
                "options": ["Book", "Chair", "Shoe", "Cup"],
                "answer": "Book",
                "help": "We read a book."
            },
            {
                "question": "What do we use to write?",
                "options": ["Pen", "Plate", "Shoe", "Bed"],
                "answer": "Pen",
                "help": "We use a pen to write."
            },
            {
                "question": "What do we drink?",
                "options": ["Water", "Book", "Table", "Bag"],
                "answer": "Water",
                "help": "We drink water."
            },
            {
                "question": "Where do students learn?",
                "options": ["School", "Kitchen", "Garden", "Garage"],
                "answer": "School",
                "help": "Students learn at school."
            },
            {
                "question": "What do we sit on?",
                "options": ["Chair", "Book", "Pen", "Cup"],
                "answer": "Chair",
                "help": "We sit on a chair."
            },
            {
                "question": "What do we wear on our feet?",
                "options": ["Shoes", "Hat", "Shirt", "Gloves"],
                "answer": "Shoes",
                "help": "We wear shoes on our feet."
            },
            {
                "question": "What do we use to carry things?",
                "options": ["Bag", "Cup", "Bed", "Plate"],
                "answer": "Bag",
                "help": "A bag can carry things."
            },
            {
                "question": "Where do we sleep?",
                "options": ["Bed", "Table", "Chair", "School"],
                "answer": "Bed",
                "help": "We sleep on a bed."
            },
            {
                "question": "What do we eat food from?",
                "options": ["Plate", "Shoe", "Book", "Pen"],
                "answer": "Plate",
                "help": "We eat food from a plate."
            },
            {
                "question": "What do we use to tell time?",
                "options": ["Clock", "Book", "Cup", "Bag"],
                "answer": "Clock",
                "help": "A clock tells time."
            }
        ]
    },


    # =====================================================
    # 5. FAMILY WORDS
    # =====================================================
    "family_words": {
        "title": "Family Words",
        "icon": "👨‍👩‍👧",
        "description": "Learn common words used for family members.",
        "questions": [
            {
                "question": "What do we call our female parent?",
                "options": ["Mother", "Brother", "Uncle", "Son"],
                "answer": "Mother",
                "help": "A female parent is a mother."
            },
            {
                "question": "What do we call our male parent?",
                "options": ["Father", "Sister", "Aunt", "Daughter"],
                "answer": "Father",
                "help": "A male parent is a father."
            },
            {
                "question": "What do we call a female sibling?",
                "options": ["Sister", "Brother", "Father", "Uncle"],
                "answer": "Sister",
                "help": "A female sibling is a sister."
            },
            {
                "question": "What do we call a male sibling?",
                "options": ["Brother", "Sister", "Mother", "Aunt"],
                "answer": "Brother",
                "help": "A male sibling is a brother."
            },
            {
                "question": "What do we call our mother's or father's mother?",
                "options": ["Grandmother", "Sister", "Daughter", "Aunt"],
                "answer": "Grandmother",
                "help": "Your parent's mother is your grandmother."
            },
            {
                "question": "What do we call our mother's or father's father?",
                "options": ["Grandfather", "Brother", "Son", "Uncle"],
                "answer": "Grandfather",
                "help": "Your parent's father is your grandfather."
            },
            {
                "question": "What do we call our father's or mother's sister?",
                "options": ["Aunt", "Mother", "Sister", "Daughter"],
                "answer": "Aunt",
                "help": "Your parent's sister is your aunt."
            },
            {
                "question": "What do we call our father's or mother's brother?",
                "options": ["Uncle", "Father", "Brother", "Son"],
                "answer": "Uncle",
                "help": "Your parent's brother is your uncle."
            },
            {
                "question": "What do parents call their male child?",
                "options": ["Son", "Daughter", "Mother", "Sister"],
                "answer": "Son",
                "help": "A male child is a son."
            },
            {
                "question": "What do parents call their female child?",
                "options": ["Daughter", "Son", "Father", "Brother"],
                "answer": "Daughter",
                "help": "A female child is a daughter."
            }
        ]
    },


    # =====================================================
    # 6. FOOD WORDS
    # =====================================================
    "food_words": {
        "title": "Food Words",
        "icon": "🍎",
        "description": "Learn common English words for food and drinks.",
        "questions": [
            {
                "question": "Which is a fruit?",
                "options": ["Apple", "Chair", "Book", "Shoe"],
                "answer": "Apple",
                "help": "Apple is a fruit."
            },
            {
                "question": "Which food is usually yellow and long?",
                "options": ["Banana", "Rice", "Bread", "Milk"],
                "answer": "Banana",
                "help": "A banana is usually yellow and long."
            },
            {
                "question": "Which drink comes from cows?",
                "options": ["Milk", "Rice", "Bread", "Apple"],
                "answer": "Milk",
                "help": "Milk can come from cows."
            },
            {
                "question": "Which food is made from wheat and often sliced?",
                "options": ["Bread", "Apple", "Milk", "Rice"],
                "answer": "Bread",
                "help": "Bread is often made from wheat."
            },
            {
                "question": "Which food is commonly cooked and eaten as grains?",
                "options": ["Rice", "Milk", "Apple", "Egg"],
                "answer": "Rice",
                "help": "Rice is a common grain food."
            },
            {
                "question": "Which food comes from a chicken?",
                "options": ["Egg", "Apple", "Bread", "Rice"],
                "answer": "Egg",
                "help": "Chickens lay eggs."
            },
            {
                "question": "Which is a red fruit?",
                "options": ["Apple", "Rice", "Milk", "Bread"],
                "answer": "Apple",
                "help": "An apple can be red."
            },
            {
                "question": "Which food is often used to make a sandwich?",
                "options": ["Bread", "Milk", "Rice", "Banana"],
                "answer": "Bread",
                "help": "Bread is commonly used for sandwiches."
            },
            {
                "question": "Which one is a drink?",
                "options": ["Milk", "Bread", "Rice", "Egg"],
                "answer": "Milk",
                "help": "Milk is a drink."
            },
            {
                "question": "Which one is a fruit?",
                "options": ["Banana", "Bread", "Egg", "Rice"],
                "answer": "Banana",
                "help": "Banana is a fruit."
            }
        ]
    },


    # =====================================================
    # 7. COLORS
    # =====================================================
    "colors": {
        "title": "Colors",
        "icon": "🎨",
        "description": "Learn common English color words.",
        "questions": [
            {
                "question": "What color is the sky on a clear day?",
                "options": ["Blue", "Green", "Black", "Pink"],
                "answer": "Blue",
                "help": "A clear daytime sky is usually blue."
            },
            {
                "question": "What color is grass usually?",
                "options": ["Green", "Red", "Black", "Purple"],
                "answer": "Green",
                "help": "Grass is usually green."
            },
            {
                "question": "What color is a ripe banana usually?",
                "options": ["Yellow", "Blue", "Black", "Purple"],
                "answer": "Yellow",
                "help": "A ripe banana is usually yellow."
            },
            {
                "question": "What color is coal usually?",
                "options": ["Black", "Pink", "Yellow", "White"],
                "answer": "Black",
                "help": "Coal is usually black."
            },
            {
                "question": "What color is milk usually?",
                "options": ["White", "Blue", "Green", "Orange"],
                "answer": "White",
                "help": "Milk is usually white."
            },
            {
                "question": "Which color is commonly associated with an orange fruit?",
                "options": ["Orange", "Blue", "Black", "Purple"],
                "answer": "Orange",
                "help": "An orange fruit is commonly orange."
            },
            {
                "question": "Which color is commonly associated with roses?",
                "options": ["Red", "Black", "Blue", "Green"],
                "answer": "Red",
                "help": "Red roses are very common."
            },
            {
                "question": "Which color is between red and blue in a rainbow?",
                "options": ["Purple", "Green", "Black", "Brown"],
                "answer": "Purple",
                "help": "Red and blue can combine to make purple."
            },
            {
                "question": "Which color is often used for tree trunks?",
                "options": ["Brown", "Pink", "Blue", "Yellow"],
                "answer": "Brown",
                "help": "Tree trunks are often brown."
            },
            {
                "question": "Which color is commonly associated with a flamingo?",
                "options": ["Pink", "Green", "Black", "Blue"],
                "answer": "Pink",
                "help": "Flamingos are commonly pink."
            }
        ]
    },


    # =====================================================
    # 8. NUMBERS
    # =====================================================
    "numbers": {
        "title": "Numbers",
        "icon": "🔢",
        "description": "Learn and recognize basic numbers.",
        "questions": [
            {
                "question": "What number comes after 1?",
                "options": ["2", "3", "4", "5"],
                "answer": "2",
                "help": "2 comes after 1."
            },
            {
                "question": "What number comes after 4?",
                "options": ["3", "5", "6", "7"],
                "answer": "5",
                "help": "5 comes after 4."
            },
            {
                "question": "What number comes before 5?",
                "options": ["3", "4", "6", "7"],
                "answer": "4",
                "help": "4 comes before 5."
            },
            {
                "question": "How many fingers are on one hand?",
                "options": ["4", "5", "6", "7"],
                "answer": "5",
                "help": "One hand has five fingers."
            },
            {
                "question": "What number comes after 7?",
                "options": ["6", "8", "9", "10"],
                "answer": "8",
                "help": "8 comes after 7."
            },
            {
                "question": "What number comes before 10?",
                "options": ["7", "8", "9", "11"],
                "answer": "9",
                "help": "9 comes before 10."
            },
            {
                "question": "What is 2 + 1?",
                "options": ["2", "3", "4", "5"],
                "answer": "3",
                "help": "2 plus 1 equals 3."
            },
            {
                "question": "What is 3 + 2?",
                "options": ["4", "5", "6", "7"],
                "answer": "5",
                "help": "3 plus 2 equals 5."
            },
            {
                "question": "Which number is the largest?",
                "options": ["2", "5", "3", "1"],
                "answer": "5",
                "help": "5 is the largest number here."
            },
            {
                "question": "Which number is the smallest?",
                "options": ["8", "4", "2", "6"],
                "answer": "2",
                "help": "2 is the smallest number here."
            }
        ]
    },


    # =====================================================
    # 9. ANIMALS
    # =====================================================
    "animals": {
        "title": "Animals",
        "icon": "🐶",
        "description": "Learn common English words for animals.",
        "questions": [
            {
                "question": "Which animal says 'meow'?",
                "options": ["Cat", "Dog", "Cow", "Horse"],
                "answer": "Cat",
                "help": "A cat says meow."
            },
            {
                "question": "Which animal says 'woof'?",
                "options": ["Dog", "Cat", "Fish", "Bird"],
                "answer": "Dog",
                "help": "A dog can bark or woof."
            },
            {
                "question": "Which animal gives us milk?",
                "options": ["Cow", "Lion", "Tiger", "Bird"],
                "answer": "Cow",
                "help": "Cows can provide milk."
            },
            {
                "question": "Which animal can fly?",
                "options": ["Bird", "Cow", "Dog", "Horse"],
                "answer": "Bird",
                "help": "Birds can fly."
            },
            {
                "question": "Which animal lives in water?",
                "options": ["Fish", "Horse", "Cow", "Dog"],
                "answer": "Fish",
                "help": "Fish live in water."
            },
            {
                "question": "Which animal is known as the king of the jungle?",
                "options": ["Lion", "Rabbit", "Fish", "Cow"],
                "answer": "Lion",
                "help": "The lion is commonly called the king of the jungle."
            },
            {
                "question": "Which animal has a long trunk?",
                "options": ["Elephant", "Cat", "Dog", "Rabbit"],
                "answer": "Elephant",
                "help": "An elephant has a long trunk."
            },
            {
                "question": "Which animal has stripes?",
                "options": ["Tiger", "Cow", "Fish", "Rabbit"],
                "answer": "Tiger",
                "help": "Tigers have stripes."
            },
            {
                "question": "Which animal can hop?",
                "options": ["Rabbit", "Cow", "Fish", "Horse"],
                "answer": "Rabbit",
                "help": "Rabbits can hop."
            },
            {
                "question": "Which animal can run and is often ridden?",
                "options": ["Horse", "Fish", "Bird", "Cat"],
                "answer": "Horse",
                "help": "People can ride horses."
            }
        ]
    },


    # =====================================================
    # 10. SIMPLE SENTENCES
    # =====================================================
    "simple_sentences": {
        "title": "Simple Sentences",
        "icon": "💬",
        "description": "Learn simple English sentences used in everyday life.",
        "questions": [
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "I am happy.",
                    "I happy am.",
                    "Am happy I.",
                    "Happy I am?"
                ],
                "answer": "I am happy.",
                "help": "The correct sentence is 'I am happy.'"
            },
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "She is a teacher.",
                    "She a teacher is.",
                    "Teacher she is a.",
                    "Is teacher she."
                ],
                "answer": "She is a teacher.",
                "help": "The correct order is subject + is + noun."
            },
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "He is my friend.",
                    "He my friend is.",
                    "Is he friend my.",
                    "Friend my he is."
                ],
                "answer": "He is my friend.",
                "help": "The correct sentence is 'He is my friend.'"
            },
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "I like apples.",
                    "I apples like.",
                    "Like I apples.",
                    "Apples I like?"
                ],
                "answer": "I like apples.",
                "help": "The correct sentence is 'I like apples.'"
            },
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "This is a book.",
                    "This a book is.",
                    "A book this is.",
                    "Book is this a."
                ],
                "answer": "This is a book.",
                "help": "The correct sentence is 'This is a book.'"
            },
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "We are students.",
                    "We students are.",
                    "Students we are?",
                    "Are students we."
                ],
                "answer": "We are students.",
                "help": "The correct sentence is 'We are students.'"
            },
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "They are happy.",
                    "They happy are.",
                    "Happy they are?",
                    "Are happy they."
                ],
                "answer": "They are happy.",
                "help": "The correct sentence is 'They are happy.'"
            },
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "I have a pen.",
                    "I a pen have.",
                    "Have pen I a.",
                    "A pen I have?"
                ],
                "answer": "I have a pen.",
                "help": "The correct sentence is 'I have a pen.'"
            },
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "She likes food.",
                    "She food likes.",
                    "Likes she food.",
                    "Food she is likes."
                ],
                "answer": "She likes food.",
                "help": "The correct sentence is 'She likes food.'"
            },
            {
                "question": "Choose the correct sentence.",
                "options": [
                    "I go to school.",
                    "I school go to.",
                    "Go school I to.",
                    "School to I go."
                ],
                "answer": "I go to school.",
                "help": "The correct sentence is 'I go to school.'"
            }
        ]
    }

}
# =========================================================
# INTELLEARN - LEVEL BASED LEARNING PATH
# =========================================================

LEARNING_LEVELS = [
    {
        "level": 1,
        "lesson": "alphabet",
        "title": "Alphabet",
        "icon": "🔤"
    },
    {
        "level": 2,
        "lesson": "sounds",
        "title": "Letter Sounds",
        "icon": "🔊"
    },
    {
        "level": 3,
        "lesson": "alphabet_examples",
        "title": "Alphabet Examples",
        "icon": "🅰️"
    },
    {
        "level": 4,
        "lesson": "basic_words",
        "title": "Basic Words",
        "icon": "📖"
    },
    {
        "level": 5,
        "lesson": "family_words",
        "title": "Family Words",
        "icon": "👨‍👩‍👧"
    },
    {
        "level": 6,
        "lesson": "food_words",
        "title": "Food Words",
        "icon": "🍎"
    },
    {
        "level": 7,
        "lesson": "colors",
        "title": "Colors",
        "icon": "🎨"
    },
    {
        "level": 8,
        "lesson": "numbers",
        "title": "Numbers",
        "icon": "🔢"
    },
    {
        "level": 9,
        "lesson": "animals",
        "title": "Animals",
        "icon": "🐶"
    },
    {
        "level": 10,
        "lesson": "simple_sentences",
        "title": "Simple Sentences",
        "icon": "💬"
    }
]
# =========================================================
# ACHIEVEMENT DEFINITIONS
# =========================================================

ACHIEVEMENTS = {
    "first_lesson": {
        "title": "First Lesson",
        "icon": "📖",
        "description": "Complete your first lesson"
    },

    "xp_builder": {
        "title": "XP Builder",
        "icon": "⭐",
        "description": "Earn 50 XP"
    },

    "reading_star": {
        "title": "Reading Star",
        "icon": "📚",
        "description": "Complete reading practice"
    },

    "speaking_starter": {
        "title": "Speaking Starter",
        "icon": "🎤",
        "description": "Complete your first speaking practice"
    },

    "three_day_streak": {
        "title": "3-Day Learner",
        "icon": "🔥",
        "description": "Maintain a 3-day learning streak"
    },

    "level_up": {
        "title": "Level Up",
        "icon": "🏆",
        "description": "Reach Level 2"
    },

    "perfect_score": {
        "title": "Perfect Score",
        "icon": "💯",
        "description": "Get a perfect lesson score"
    }
}


# =========================================================
# CREATE DATABASE
# =========================================================
def create_database(): 
 
    print("Checking database...") 
 
    # ----------------------------------------------------- 
    # Check existing database 
    # ----------------------------------------------------- 
 
    if os.path.exists(DATABASE): 
 
        try: 
 
            test_connection = sqlite3.connect( 
                DATABASE 
            ) 
 
            result = test_connection.execute( 
                "PRAGMA integrity_check" 
            ).fetchone() 
 
            test_connection.close() 
 
            if result and result[0] != "ok": 
 
                print("Database is corrupted.") 
 
                timestamp = datetime.now().strftime( 
                    "%Y%m%d_%H%M%S" 
                ) 
 
                corrupted_name = ( 
                    f"database_corrupted_{timestamp}.db" 
                ) 
 
                os.rename( 
                    DATABASE, 
                    corrupted_name 
                ) 
 
                print( 
                    "Corrupted database renamed to:", 
                    corrupted_name 
                ) 
 
        except sqlite3.DatabaseError: 
 
            print("Database is malformed.") 
 
            timestamp = datetime.now().strftime( 
                "%Y%m%d_%H%M%S" 
            ) 
 
            corrupted_name = ( 
                f"database_corrupted_{timestamp}.db" 
            ) 
 
            try: 
 
                os.rename( 
                    DATABASE, 
                    corrupted_name 
                ) 
 
                print( 
                    "Corrupted database renamed to:", 
                    corrupted_name 
                ) 
 
            except Exception: 
 
                pass 
 
    # ----------------------------------------------------- 
    # Connection 
    # ----------------------------------------------------- 
 
    connection = get_db_connection() 
 
    cursor = connection.cursor() 
 
 
    # ===================================================== 
    # USERS 
    # ===================================================== 
 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users ( 
 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
 
            name TEXT NOT NULL, 
 
            email TEXT UNIQUE NOT NULL, 
 
            password TEXT NOT NULL, 
 
            preferred_language TEXT NOT NULL, 
 
            learning_language TEXT NOT NULL, 
 
            xp INTEGER DEFAULT 0, 
 
            streak INTEGER DEFAULT 0, 
 
            level INTEGER DEFAULT 1 
        ) 
    """) 
 
 
    # ===================================================== 
    # MILESTONE 2 - LEARNER SKILL PERFORMANCE 
    # ===================================================== 
 
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS learner_skill_performance ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_id INTEGER NOT NULL, 
        skill TEXT NOT NULL, 
        correct_answers INTEGER DEFAULT 0, 
        total_answers INTEGER DEFAULT 0, 
        proficiency_score REAL DEFAULT 0, 
        proficiency_level TEXT DEFAULT 'Beginner', 
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        FOREIGN KEY (user_id) REFERENCES users(id))""") 
 
    # ===================================================== 
    # USER PROGRESS 
    # ===================================================== 
 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS user_progress ( 
 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
 
            user_id INTEGER UNIQUE NOT NULL, 
 
            reading_progress INTEGER DEFAULT 0, 
 
            writing_progress INTEGER DEFAULT 0, 
 
            speaking_progress INTEGER DEFAULT 0, 
 
            FOREIGN KEY(user_id) 
            REFERENCES users(id) 
        ) 
    """) 
 
 
    # ===================================================== 
    # ASSESSMENT QUESTIONS 
    # ===================================================== 
 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS assessment_questions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    language TEXT NOT NULL DEFAULT 'English',

    question TEXT NOT NULL,

    option_a TEXT NOT NULL,

    option_b TEXT NOT NULL,

    option_c TEXT NOT NULL,

    option_d TEXT NOT NULL,

    correct_answer TEXT NOT NULL,

    skill TEXT NOT NULL,

    difficulty TEXT DEFAULT 'Beginner'
        ) 

    """)
        # -----------------------------------------------------
    # ADD LANGUAGE COLUMN TO OLD DATABASE
    # -----------------------------------------------------

    columns = [
        row["name"]
        for row in cursor.execute(
            "PRAGMA table_info(assessment_questions)"
        ).fetchall()
    ]

    if "language" not in columns:

        cursor.execute(
            """
            ALTER TABLE assessment_questions
            ADD COLUMN language TEXT NOT NULL DEFAULT 'English'
            """
        ) 
 
 
    # ===================================================== 
    # ASSESSMENT ATTEMPTS 
    # ===================================================== 
 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS assessment_attempts ( 
 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
 
            user_id INTEGER NOT NULL, 
 
            score INTEGER NOT NULL, 
 
            total_questions INTEGER NOT NULL, 
 
            proficiency_level TEXT NOT NULL, 
 
            created_at TIMESTAMP 
            DEFAULT CURRENT_TIMESTAMP, 
 
            FOREIGN KEY(user_id) 
            REFERENCES users(id) 
        ) 
    """) 
 
 
    # ===================================================== 
    # ASSESSMENT ANSWERS 
    # ===================================================== 
 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS assessment_answers ( 
 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
 
            attempt_id INTEGER NOT NULL, 
 
            question_id INTEGER NOT NULL, 
 
            selected_answer TEXT, 
 
            is_correct INTEGER DEFAULT 0, 
 
            FOREIGN KEY(attempt_id) 
            REFERENCES assessment_attempts(id), 
 
            FOREIGN KEY(question_id) 
            REFERENCES assessment_questions(id) 
        ) 
    """) 
 
 
    # ===================================================== 
    # LEARNING QUESTIONS 
    # Kept for compatibility with your existing database 
    # ===================================================== 
 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS learning_questions ( 
 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
 
            lesson TEXT NOT NULL, 
 
            question_type TEXT NOT NULL, 
 
            question TEXT NOT NULL, 
 
            option_a TEXT NOT NULL, 
 
            option_b TEXT NOT NULL, 
 
            option_c TEXT NOT NULL, 
 
            option_d TEXT NOT NULL, 
 
            correct_answer TEXT NOT NULL, 
 
            explanation TEXT, 
 
            xp INTEGER DEFAULT 10 
        ) 
    """) 
 
 
    # ===================================================== 
    # LESSON PROGRESS 
    # ===================================================== 
 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS lesson_progress ( 
 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
 
            user_id INTEGER NOT NULL, 
 
            lesson TEXT NOT NULL, 
 
            completed INTEGER DEFAULT 0, 
 
            best_score INTEGER DEFAULT 0, 
 
            total_questions INTEGER DEFAULT 0, 
 
            attempts INTEGER DEFAULT 0, 
 
            last_attempt TIMESTAMP 
            DEFAULT CURRENT_TIMESTAMP, 
 
            UNIQUE(user_id, lesson), 
 
            FOREIGN KEY(user_id) 
            REFERENCES users(id) 
        ) 
    """) 
 
 
    # ========================================================= 
    # MILESTONE 2 - LEARNING PATH 
    # ========================================================= 
 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS learning_paths ( 
 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
 
            user_id INTEGER NOT NULL, 
 
            lesson TEXT NOT NULL, 
 
            position INTEGER NOT NULL, 
 
            status TEXT DEFAULT 'not_started', 
 
            score INTEGER DEFAULT 0, 
 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
 
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
 
            UNIQUE(user_id, lesson), 
 
            FOREIGN KEY(user_id) 
            REFERENCES users(id) 
        ) 
    """) 
 
 
    # ===================================================== 
    # ASSESSMENT SEED QUESTIONS 
    # ===================================================== 
 
    assessment_questions = [

    # =====================================================
    # ENGLISH - 9 QUESTIONS
    # =====================================================

    (
        "English",
        "Which word starts with the letter B?",
        "Cat",
        "Ball",
        "Apple",
        "Dog",
        "B",
        "Reading",
        "Beginner"
    ),

    (
        "English",
        "Which word means a place where you live?",
        "House",
        "Book",
        "Pen",
        "Table",
        "A",
        "Reading",
        "Beginner"
    ),

    (
        "English",
        "Choose the correct word: I ___ a book.",
        "read",
        "blue",
        "jump",
        "cold",
        "A",
        "Reading",
        "Beginner"
    ),

    (
        "English",
        "Which spelling is correct?",
        "Skool",
        "Scool",
        "School",
        "Schol",
        "C",
        "Writing",
        "Beginner"
    ),

    (
        "English",
        "Which word is spelled correctly?",
        "Frend",
        "Friend",
        "Freind",
        "Frind",
        "B",
        "Writing",
        "Beginner"
    ),

    (
        "English",
        "Complete the word: C _ T",
        "A",
        "E",
        "I",
        "O",
        "A",
        "Writing",
        "Beginner"
    ),

    (
        "English",
        "Ravi has a red ball. What color is Ravi's ball?",
        "Blue",
        "Green",
        "Red",
        "Yellow",
        "C",
        "Comprehension",
        "Beginner"
    ),

    (
        "English",
        "Anita drinks water every morning. What does Anita drink?",
        "Milk",
        "Water",
        "Juice",
        "Tea",
        "B",
        "Comprehension",
        "Beginner"
    ),

    (
        "English",
        "John goes to school at 9 AM. Where does John go?",
        "Market",
        "Hospital",
        "School",
        "Park",
        "C",
        "Comprehension",
        "Beginner"
    ),


    # =====================================================
    # TELUGU - 9 QUESTIONS
    # =====================================================

    (
        "Telugu",
        "B అక్షరంతో ప్రారంభమయ్యే పదం ఏది?",
        "పిల్లి",
        "బంతి",
        "ఆపిల్",
        "కుక్క",
        "B",
        "Reading",
        "Beginner"
    ),

    (
        "Telugu",
        "మీరు నివసించే ప్రదేశాన్ని సూచించే పదం ఏది?",
        "ఇల్లు",
        "పుస్తకం",
        "పెన్",
        "బల్ల",
        "A",
        "Reading",
        "Beginner"
    ),

    (
        "Telugu",
        "సరైన పదాన్ని ఎంచుకోండి: నేను ___ పుస్తకం.",
        "చదువుతాను",
        "నీలం",
        "దూకుతాను",
        "చల్లగా",
        "A",
        "Reading",
        "Beginner"
    ),

    (
        "Telugu",
        "సరైన పదం ఏది?",
        "స్కూల్",
        "స్కుల్",
        "పాఠశాల",
        "స్కోల్",
        "C",
        "Writing",
        "Beginner"
    ),

    (
        "Telugu",
        "సరిగ్గా వ్రాయబడిన పదం ఏది?",
        "ఫ్రెండ్",
        "స్నేహితుడు",
        "ఫ్రెయిండ్",
        "ఫ్రిండ్",
        "B",
        "Writing",
        "Beginner"
    ),

    (
        "Telugu",
        "పదాన్ని పూర్తి చేయండి: C _ T",
        "A",
        "E",
        "I",
        "O",
        "A",
        "Writing",
        "Beginner"
    ),

    (
        "Telugu",
        "రవి దగ్గర ఎరుపు రంగు బంతి ఉంది. రవి బంతి ఏ రంగులో ఉంది?",
        "నీలం",
        "ఆకుపచ్చ",
        "ఎరుపు",
        "పసుపు",
        "C",
        "Comprehension",
        "Beginner"
    ),

    (
        "Telugu",
        "అనిత ప్రతి ఉదయం నీరు తాగుతుంది. అనిత ఏమి తాగుతుంది?",
        "పాలు",
        "నీరు",
        "రసం",
        "టీ",
        "B",
        "Comprehension",
        "Beginner"
    ),

    (
        "Telugu",
        "జాన్ ఉదయం 9 గంటలకు పాఠశాలకు వెళ్తాడు. జాన్ ఎక్కడికి వెళ్తాడు?",
        "మార్కెట్",
        "ఆసుపత్రి",
        "పాఠశాల",
        "పార్క్",
        "C",
        "Comprehension",
        "Beginner"
    ),


    # =====================================================
    # HINDI - 9 QUESTIONS
    # =====================================================

    (
        "Hindi",
        "B अक्षर से शुरू होने वाला शब्द कौन सा है?",
        "बिल्ली",
        "गेंद",
        "सेब",
        "कुत्ता",
        "B",
        "Reading",
        "Beginner"
    ),

    (
        "Hindi",
        "वह शब्द कौन सा है जिसका अर्थ है जहाँ आप रहते हैं?",
        "घर",
        "किताब",
        "कलम",
        "मेज",
        "A",
        "Reading",
        "Beginner"
    ),

    (
        "Hindi",
        "सही शब्द चुनें: मैं ___ एक किताब।",
        "पढ़ता हूँ",
        "नीला",
        "कूदता हूँ",
        "ठंडा",
        "A",
        "Reading",
        "Beginner"
    ),

    (
        "Hindi",
        "सही शब्द कौन सा है?",
        "स्कूल",
        "स्कुल",
        "विद्यालय",
        "स्कोल",
        "C",
        "Writing",
        "Beginner"
    ),

    (
        "Hindi",
        "सही लिखा हुआ शब्द कौन सा है?",
        "फ्रेंड",
        "दोस्त",
        "फ्रेइंड",
        "फ्रिंड",
        "B",
        "Writing",
        "Beginner"
    ),

    (
        "Hindi",
        "शब्द पूरा करें: C _ T",
        "A",
        "E",
        "I",
        "O",
        "A",
        "Writing",
        "Beginner"
    ),

    (
        "Hindi",
        "रवि के पास लाल रंग की गेंद है। रवि की गेंद किस रंग की है?",
        "नीला",
        "हरा",
        "लाल",
        "पीला",
        "C",
        "Comprehension",
        "Beginner"
    ),

    (
        "Hindi",
        "अनिता हर सुबह पानी पीती है। अनिता क्या पीती है?",
        "दूध",
        "पानी",
        "जूस",
        "चाय",
        "B",
        "Comprehension",
        "Beginner"
    ),

    (
        "Hindi",
        "जॉन सुबह 9 बजे स्कूल जाता है। जॉन कहाँ जाता है?",
        "बाज़ार",
        "अस्पताल",
        "स्कूल",
        "पार्क",
        "C",
        "Comprehension",
        "Beginner"
    )
]

    languages = ["English", "Telugu", "Hindi"]
    for language in languages:
        language_count = cursor.execute(
        """
        SELECT COUNT(*)
        FROM assessment_questions
        WHERE language = ?
        """,
        (language,)
    ).fetchone()[0]

    if language_count == 0:

        language_questions = [
            question
            for question in assessment_questions
            if question[0] == language
        ]

        cursor.executemany(
            """
            INSERT INTO assessment_questions
            (
                language,
                question,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                skill,
                difficulty
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            language_questions
        )
 
 
    
      
 
 
    # ===================================================== 
    # CREATE MISSING PROGRESS ROWS 
    # ===================================================== 
 
    cursor.execute(""" 
        INSERT OR IGNORE INTO user_progress 
        ( 
            user_id, 
            reading_progress, 
            writing_progress, 
            speaking_progress 
        ) 
        SELECT 
            id, 
            0, 
            0, 
            0 
        FROM users 
    """) 
     # =========================================================
    # ACHIEVEMENTS TABLE
    # =========================================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            achievement_key TEXT NOT NULL,
            unlocked_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, achievement_key),
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
 
    connection.commit() 
 
    connection.close() 
 
    print("Database ready.") 
# =========================================================
# UPDATE USER LEVEL
# =========================================================

def update_user_level(user_id):

    connection = get_db_connection()

    user = connection.execute(
        """
        SELECT xp
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    ).fetchone()

    if not user:

        connection.close()

        return

    xp = user["xp"]


    if xp < 100:

        level = 1

    elif xp < 250:

        level = 2

    elif xp < 500:

        level = 3

    elif xp < 800:

        level = 4

    else:

        level = 5


    connection.execute(
        """
        UPDATE users
        SET level = ?
        WHERE id = ?
        """,
        (
            level,
            user_id
        )
    )

    connection.commit()

    connection.close()


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# =========================================================
# PWA SERVICE WORKER
# =========================================================

@app.route("/service-worker.js")
def service_worker():

    return app.send_static_file("service-worker.js")
# =========================================================
# REGISTER
# =========================================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        )

        preferred_language = request.form.get(
            "preferred_language",
            "English"
        )

        learning_language = request.form.get(
            "learning_language",
            "English"
        )


        if not name or not email or not password:

            return """
            <h2>Please fill all required fields.</h2>
            <a href="/register">Go back</a>
            """


        connection = get_db_connection()

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO users
                (
                    name,
                    email,
                    password,
                    preferred_language,
                    learning_language,
                    xp,
                    streak,
                    level
                )
                VALUES (?, ?, ?, ?, ?, 0, 0, 1)
                """,
                (
                    name,
                    email,
                    password,
                    preferred_language,
                    learning_language
                )
            )

            user_id = cursor.lastrowid


            cursor.execute(
                """
                INSERT INTO user_progress
                (
                    user_id,
                    reading_progress,
                    writing_progress,
                    speaking_progress
                )
                VALUES (?, 0, 0, 0)
                """,
                (
                    user_id,
                )
            )


            connection.commit()

            connection.close()

            return redirect("/login")


        except sqlite3.IntegrityError:

            connection.close()

            return """
            <h2>Email already registered.</h2>

            <a href="/register">
                Go back to Register
            </a>
            """


    return render_template(
        "register.html"
    )


# =========================================================
# LOGIN
# =========================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip()

        password = request.form.get("password", "")

        connection = get_db_connection()

        user = connection.execute(
            """
            SELECT *
            FROM users
            WHERE email = ? AND password = ?
            """,
            (email, password)
        ).fetchone()

        connection.close()

        if user:

            session["user_id"] = user["id"]

            session["preferred_language"] = (
                user["preferred_language"].strip()
            )

            session["learning_language"] = (
                user["learning_language"].strip()
            )

            print("==============================")
            print("LOGIN SUCCESS")
            print(
                "Preferred Language:",
                session["preferred_language"]
            )
            print(
                "Learning Language:",
                session["learning_language"]
            )
            print("==============================")

            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Invalid email or password"
        )

    return render_template("login.html")

# =========================================================
# DASHBOARD
# =========================================================
# =========================================================
# BEAUTIFUL DASHBOARD
# =========================================================

# =========================================================
# MILESTONE 2 - ADAPTIVE LEARNING RECOMMENDATION MODEL
# =========================================================
# =====================================================
# LEARNER PROFICIENCY PREDICTION
# =====================================================

def predict_learner_proficiency(user_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    # -------------------------------------------------
    # 1. Get latest assessment score
    # -------------------------------------------------

    cursor.execute(
        """
        SELECT score, total_questions
        FROM assessment_attempts
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (user_id,)
    )

    assessment = cursor.fetchone()

    if assessment:

        assessment_score = round(
            (assessment["score"] / assessment["total_questions"]) * 100
        )

    else:

        assessment_score = 0


    # -------------------------------------------------
    # 2. Get lesson performance
    # -------------------------------------------------

    cursor.execute(
        """
        SELECT AVG(proficiency_score) AS avg_score
        FROM learner_skill_performance
        WHERE user_id = ?
        AND skill NOT IN (
            'Reading',
            'Writing',
            'Comprehension'
        )
        """,
        (user_id,)
    )

    lesson_result = cursor.fetchone()

    if lesson_result and lesson_result["avg_score"] is not None:

        lesson_score = round(
            lesson_result["avg_score"]
        )

    else:

        lesson_score = 0


    # -------------------------------------------------
    # 3. Get learning progress
    # -------------------------------------------------

    cursor.execute(
        """
        SELECT reading_progress,
               writing_progress,
               speaking_progress
        FROM user_progress
        WHERE user_id = ?
        """,
        (user_id,)
    )

    progress = cursor.fetchone()

    if progress:

        progress_score = round(
            (
                progress["reading_progress"]
                +
                progress["writing_progress"]
                +
                progress["speaking_progress"]
            ) / 3
        )

    else:

        progress_score = 0


    # -------------------------------------------------
    # 4. Calculate predicted proficiency
    # -------------------------------------------------

    predicted_score = round(
        (assessment_score * 0.40)
        +
        (lesson_score * 0.35)
        +
        (progress_score * 0.25)
    )


    # -------------------------------------------------
    # 5. Determine proficiency level
    # -------------------------------------------------

    if predicted_score < 40:

        predicted_level = "Beginner"

    elif predicted_score < 60:

        predicted_level = "Basic"

    elif predicted_score < 80:

        predicted_level = "Intermediate"

    else:

        predicted_level = "Advanced"


    conn.close()


    # -------------------------------------------------
    # 6. Return prediction
    # -------------------------------------------------

    return {
        "score": predicted_score,
        "level": predicted_level,
        "assessment_score": assessment_score,
        "lesson_score": lesson_score,
        "progress_score": progress_score
    }
# =========================================================
# LEARNING PATH LANGUAGE TRANSLATIONS
# =========================================================

LEARNING_PATH_TRANSLATIONS = {

    "English": {
        "title": "Learning Path",
        "level": "Level",
        "completed": "Completed",
        "current": "Current Level",
        "locked": "Locked",
        "complete_previous": "Complete the previous level to unlock",
        "start": "Start",
        "review": "Review",
        "personalized": "Personalized"
    },

    "Telugu": {
        "title": "మీ అభ్యాస మార్గం",
        "level": "స్థాయి",
        "completed": "పూర్తి చేశారు",
        "current": "ప్రస్తుత స్థాయి",
        "locked": "లాక్ చేయబడింది",
        "complete_previous": "మునుపటి స్థాయిని పూర్తి చేయండి",
        "start": "ప్రారంభించండి",
        "review": "మళ్లీ చూడండి",
        "personalized": "వ్యక్తిగతీకరించబడింది"
    },

    "Hindi": {
        "title": "आपकी सीखने की यात्रा",
        "level": "स्तर",
        "completed": "पूर्ण",
        "current": "वर्तमान स्तर",
        "locked": "लॉक है",
        "complete_previous": "पिछला स्तर पूरा करें",
        "start": "शुरू करें",
        "review": "दोबारा देखें",
        "personalized": "व्यक्तिगत"
    }
}
# =========================================================
# GET LEVEL BASED LEARNING PATH
# =========================================================
# =========================================================
# GET LEVEL BASED LEARNING PATH
# =========================================================

def get_learning_path_levels(user_id):
    """
    Creates a sequential learning path.

    A level becomes available only when the previous
    level has been completed with a score of 60% or more.
    """

    connection = get_db_connection()

    progress_rows = connection.execute(
        """
        SELECT lesson,
               completed,
               best_score
        FROM lesson_progress
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchall()

    connection.close()

    progress = {
        row["lesson"]: row
        for row in progress_rows
    }

    localized_lessons = get_localized_lessons()

    learning_path = []

    # Level 1 is always unlocked
    previous_passed = True

    for level_data in LEARNING_LEVELS:

        lesson_name = level_data["lesson"]

        row = progress.get(lesson_name)

        completed = False
        score = 0

        if row:

            completed = bool(
                row["completed"]
            )

            try:
                raw_score = float(row["best_score"] or 0)

    # best_score is stored as number of correct answers out of 10
                score = round((raw_score / 10) * 100)
            except (
                TypeError,
                ValueError
                ):
                score = 0

        # -------------------------------------------------
        # CHECK CURRENT LEVEL
        # -------------------------------------------------

        passed = (
            completed
            and score >= 60
        )

        # -------------------------------------------------
        # DETERMINE STATUS
        # -------------------------------------------------

        if passed:

            status = "completed"

            unlocked = True

        elif previous_passed:

            status = "current"

            unlocked = True

        else:

            status = "locked"

            unlocked = False

        # -------------------------------------------------
        # ADD LEVEL
        # -------------------------------------------------

        learning_path.append(
            {
                "level": level_data["level"],

                "lesson": lesson_name,

                "title": localized_lessons.get(
                    lesson_name,
                    LESSONS.get(
                        lesson_name,
                        {}
                    )
                ).get(
                    "title",
                    lesson_name.replace(
                        "_",
                        " "
                    ).title()
                ),

                "icon": level_data["icon"],

                "completed": passed,

                "score": score,

                "status": status,

                "unlocked": unlocked
            }
        )

        # -------------------------------------------------
        # IMPORTANT:
        # NEXT LEVEL DEPENDS ON THIS LEVEL
        # -------------------------------------------------

        previous_passed = passed

    return learning_path
        

        # -------------------------------------------------
        # NEXT LEVEL CAN ONLY UNLOCK IF THIS LEVEL PASSED
        # -------------------------------------------------

    previous_unlocked = passed

    return learning_path
def get_adaptive_recommendation(user_id):
    """
    Select the next learning activity from the learner's latest
    performance.

    Strategy:
    1. Use only the latest performance record for each lesson/skill.
    2. Give priority to weak skills (< 60%).
    3. Then consider developing skills (60-79%).
    4. If there is no performance yet, start with the first lesson.
    5. If the learner has mastered available lessons, recommend the
       lowest-scoring lesson for reinforcement.

    This is a deterministic adaptive recommendation model, so it
    works without an external AI service or additional database table.
    """

    connection = get_db_connection()

    # Latest performance for every lesson/skill.
    performance_rows = connection.execute(
        """
        SELECT lsp.skill,
               lsp.correct_answers,
               lsp.total_answers,
               lsp.proficiency_score,
               lsp.proficiency_level
        FROM learner_skill_performance AS lsp
        INNER JOIN (
            SELECT skill, MAX(id) AS latest_id
            FROM learner_skill_performance
            WHERE user_id = ?
            GROUP BY skill
        ) AS latest
            ON lsp.skill = latest.skill
           AND lsp.id = latest.latest_id
        WHERE lsp.user_id = ?
        """,
        (user_id, user_id)
    ).fetchall()

    completed_rows = connection.execute(
        """
        SELECT lesson, completed, best_score, attempts
        FROM lesson_progress
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchall()

    connection.close()

    performance = {
        row["skill"]: row
        for row in performance_rows
    }

    completed = {
        row["lesson"]: row
        for row in completed_rows
    }

    # Lesson order is intentional: foundational lessons come first.
    lesson_order = [
        "alphabet",
        "sounds",
        "alphabet_examples",
        "basic_words",
        "family_words",
        "food_words",
        "colors",
        "numbers",
        "animals",
        "simple_sentences"
    ]

    # Map learning lessons to broader learner skills for explanation.
    skill_groups = {
        "alphabet": "Reading",
        "sounds": "Reading",
        "alphabet_examples": "Reading",
        "basic_words": "Reading",
        "family_words": "Reading",
        "food_words": "Reading",
        "colors": "Reading",
        "numbers": "Reading",
        "animals": "Reading",
        "simple_sentences": "Writing"
    }

    localized_lessons = get_localized_lessons()

    # -----------------------------------------------------
    # Find weak/developing lessons first.
    # Lower score = higher recommendation priority.
    # -----------------------------------------------------
    candidates = []

    for index, lesson_name in enumerate(lesson_order):

        row = performance.get(lesson_name)

        if row is None:
            continue

        try:
            score = float(row["proficiency_score"] or 0)
        except (TypeError, ValueError):
            score = 0

        if score < 60:
            priority = 1000 - score
        elif score < 80:
            priority = 500 - score
        else:
            priority = 100 - score

        candidates.append(
            (priority, index, lesson_name, row)
        )

    # Prefer a weak/developing lesson. If none exists, choose the next
    # uncompleted lesson so the learner continues progressing.
    weak_or_developing = [
        item for item in candidates
        if float(item[3]["proficiency_score"] or 0) < 80
    ]

    if weak_or_developing:
        _, _, lesson_name, row = sorted(
            weak_or_developing,
            key=lambda item: (-item[0], item[1])
        )[0]

        score = round(float(row["proficiency_score"] or 0))
        level = row["proficiency_level"] or "Beginner"
        reason_type = "weak" if score < 60 else "developing"

    else:
        uncompleted = [
            lesson_name
            for lesson_name in lesson_order
            if not completed.get(lesson_name)
            or not completed[lesson_name]["completed"]
        ]

        if uncompleted:
            lesson_name = uncompleted[0]
            row = performance.get(lesson_name)

            if row:
                score = round(float(row["proficiency_score"] or 0))
                level = row["proficiency_level"] or "Beginner"
            else:
                score = 0
                level = "Not Assessed"

            reason_type = "new"

        elif candidates:
            # All lessons are completed/mastered: reinforce the
            # lowest-scoring lesson.
            _, _, lesson_name, row = sorted(
                candidates,
                key=lambda item: (
                    float(item[3]["proficiency_score"] or 0),
                    item[1]
                )
            )[0]

            score = round(float(row["proficiency_score"] or 0))
            level = row["proficiency_level"] or "Beginner"
            reason_type = "review"

        else:
            # Brand-new learner.
            lesson_name = lesson_order[0]
            score = 0
            level = "Not Assessed"
            reason_type = "new"

    lesson = localized_lessons.get(
        lesson_name,
        LESSONS.get(lesson_name, {})
    )

    preferred_language = get_current_language()

    reasons = {
        "English": {
            "weak": f"Your score is {score}%. Practice this lesson to improve your weak area.",
            "developing": f"Your score is {score}%. More practice will help you strengthen this skill.",
            "new": "This is the next recommended lesson based on your learning path.",
            "review": f"Your score is {score}%. Review this lesson to strengthen your skills."
        },
        "Telugu": {
            "weak": f"మీ స్కోర్ {score}%. మీ బలహీనమైన అంశాన్ని మెరుగుపరచడానికి ఈ పాఠాన్ని అభ్యసించండి.",
            "developing": f"మీ స్కోర్ {score}%. ఈ నైపుణ్యాన్ని బలోపేతం చేయడానికి మరింత అభ్యాసం చేయండి.",
            "new": "మీ అభ్యాస మార్గం ఆధారంగా ఇది తదుపరి సిఫార్సు చేసిన పాఠం.",
            "review": f"మీ స్కోర్ {score}%. మీ నైపుణ్యాలను బలోపేతం చేయడానికి ఈ పాఠాన్ని మళ్లీ అభ్యసించండి."
        },
        "Hindi": {
            "weak": f"आपका स्कोर {score}% है। अपनी कमजोर क्षमता सुधारने के लिए इस पाठ का अभ्यास करें।",
            "developing": f"आपका स्कोर {score}% है। इस कौशल को मजबूत करने के लिए अधिक अभ्यास करें।",
            "new": "आपके सीखने के मार्ग के आधार पर यह अगला अनुशंसित पाठ है।",
            "review": f"आपका स्कोर {score}% है। अपने कौशल को मजबूत करने के लिए इस पाठ को दोहराएँ।"
        }
    }

    return {
        "lesson_name": lesson_name,
        "lesson_title": lesson.get("title", lesson_name.replace("_", " ").title()),
        "lesson_icon": lesson.get("icon", "📘"),
        "lesson_description": lesson.get("description", ""),
        "skill": skill_groups.get(lesson_name, "Learning"),
        "score": score,
        "proficiency_level": level,
        "reason": reasons.get(
            preferred_language,
            reasons["English"]
        )[reason_type],
        "reason_type": reason_type
    }
# =========================================================
# MILESTONE 2 - PERSONALIZED LESSON GENERATION
# =========================================================
# =========================================================
# MILESTONE 2 - CONTENT RECOMMENDATION ENGINE
# =========================================================

def get_content_recommendations(user_id):
    """
    Recommend multiple learning contents based on the learner's
    latest performance.

    Strategy:
    1. Use only the latest performance record for each lesson.
    2. Give highest priority to weak lessons (< 60%).
    3. Then prioritize developing lessons (60-79%).
    4. Recommend uncompleted lessons when there is no performance.
    5. Use completed lessons for reinforcement when appropriate.
    6. Return multiple ranked learning contents.
    """

    connection = get_db_connection()

    # Get the latest performance record for every lesson/skill.
    performance_rows = connection.execute(
        """
        SELECT lsp.skill,
               lsp.correct_answers,
               lsp.total_answers,
               lsp.proficiency_score,
               lsp.proficiency_level
        FROM learner_skill_performance AS lsp
        INNER JOIN (
            SELECT skill, MAX(id) AS latest_id
            FROM learner_skill_performance
            WHERE user_id = ?
            GROUP BY skill
        ) AS latest
            ON lsp.skill = latest.skill
           AND lsp.id = latest.latest_id
        WHERE lsp.user_id = ?
        """,
        (user_id, user_id)
    ).fetchall()

    # Get lesson completion information.
    completed_rows = connection.execute(
        """
        SELECT lesson,
               completed,
               best_score,
               attempts
        FROM lesson_progress
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchall()

    connection.close()

    performance = {
        row["skill"]: row
        for row in performance_rows
    }

    completed = {
        row["lesson"]: row
        for row in completed_rows
    }

    # The learning order is the same as the existing
    # adaptive learning path.
    lesson_order = [
        "alphabet",
        "sounds",
        "alphabet_examples",
        "basic_words",
        "family_words",
        "food_words",
        "colors",
        "numbers",
        "animals",
        "simple_sentences"
    ]

    localized_lessons = get_localized_lessons()

    recommendations = []

    # -----------------------------------------------------
    # Generate recommendation score for every lesson.
    # -----------------------------------------------------

    for index, lesson_name in enumerate(lesson_order):

        lesson = localized_lessons.get(
            lesson_name,
            LESSONS.get(lesson_name, {})
        )

        row = performance.get(lesson_name)

        # -------------------------------------------------
        # New / not assessed lesson
        # -------------------------------------------------
        if row is None:

            is_completed = (
                lesson_name in completed
                and completed[lesson_name]["completed"]
            )

            if not is_completed:
                priority = 700 - index

                reason = (
                    "This lesson is not assessed yet and is "
                    "recommended as new learning content."
                )

                reason_type = "new"
                score = 0
                proficiency_level = "Not Assessed"

            else:
                # Completed but no performance record.
                priority = 100 - index

                reason = (
                    "This lesson can be reviewed to reinforce "
                    "your learning."
                )

                reason_type = "review"
                score = 0
                proficiency_level = "Completed"

        # -------------------------------------------------
        # Existing performance
        # -------------------------------------------------
        else:

            try:
                score = round(
                    float(row["proficiency_score"] or 0)
                )
            except (TypeError, ValueError):
                score = 0

            proficiency_level = (
                row["proficiency_level"]
                or "Beginner"
            )

            is_completed = (
                lesson_name in completed
                and completed[lesson_name]["completed"]
            )

            # Weak skill
            if score < 60:

                priority = 1000 - score

                reason = (
                    f"Your score is {score}%. "
                    "This lesson needs more practice."
                )

                reason_type = "weak"

            # Developing skill
            elif score < 80:

                priority = 700 - score

                reason = (
                    f"Your score is {score}%. "
                    "More practice will help strengthen this skill."
                )

                reason_type = "developing"

            # Strong skill
            else:

                if is_completed:

                    priority = 100 - score

                    reason = (
                        f"Your score is {score}%. "
                        "Review this lesson to maintain your skills."
                    )

                    reason_type = "review"

                else:

                    priority = 600 - score

                    reason = (
                        f"Your score is {score}%. "
                        "This lesson is ready for continued learning."
                    )

                    reason_type = "strong"

        recommendations.append(
            {
                "lesson_name": lesson_name,
                "lesson_title": lesson.get(
                    "title",
                    lesson_name.replace("_", " ").title()
                ),
                "lesson_icon": lesson.get(
                    "icon",
                    "📘"
                ),
                "lesson_description": lesson.get(
                    "description",
                    ""
                ),
                "score": score,
                "proficiency_level": proficiency_level,
                "priority": priority,
                "reason": reason,
                "reason_type": reason_type,
                "completed": is_completed
            }
        )

    # -----------------------------------------------------
    # Sort recommendations.
    #
    # Higher priority = more important recommendation.
    # Lesson order is used as a tie breaker.
    # -----------------------------------------------------

    recommendations.sort(
        key=lambda item: (
            -item["priority"],
            lesson_order.index(item["lesson_name"])
        )
    )

    # -----------------------------------------------------
    # Return the top 5 recommended contents.
    # -----------------------------------------------------

    return recommendations[:5]
def generate_personalized_lesson(user_id):

    """
    Generate a personalized lesson based on the learner's
    latest proficiency and weak/developing skills.

    The workflow:
    1. Get the learner's proficiency prediction.
    2. Get the adaptive lesson recommendation.
    3. Identify the learner's current level.
    4. Select suitable questions from the recommended lesson.
    5. Return a personalized lesson.
    """

    # -----------------------------------------------------
    # 1. Get learner proficiency
    # -----------------------------------------------------

    proficiency = predict_learner_proficiency(user_id)

    predicted_level = proficiency["level"]


    # -----------------------------------------------------
    # 2. Get adaptive recommendation
    # -----------------------------------------------------

    recommendation = get_adaptive_recommendation(user_id)

    lesson_name = recommendation["lesson_name"]


    # -----------------------------------------------------
    # 3. Get original lesson
    # -----------------------------------------------------

    lesson_data = LESSONS.get(lesson_name)

    if not lesson_data:

        return None


    # -----------------------------------------------------
    # 4. Get questions
    # -----------------------------------------------------

    questions = lesson_data.get(
        "questions",
        []
    )


    # -----------------------------------------------------
    # 5. Select questions according to proficiency
    # -----------------------------------------------------

    if predicted_level == "Beginner":

        selected_questions = questions[:5]

    elif predicted_level == "Basic":

        selected_questions = questions[:7]

    elif predicted_level == "Intermediate":

        selected_questions = questions[:8]

    else:

        selected_questions = questions[:10]


    # -----------------------------------------------------
    # 6. Get localized lesson information
    # -----------------------------------------------------

    localized_lessons = get_localized_lessons()

    localized_lesson = localized_lessons.get(
        lesson_name,
        lesson_data
    )


    # -----------------------------------------------------
    # 7. Return personalized lesson
    # -----------------------------------------------------

    return {
        "lesson_name": lesson_name,

        "lesson_title": localized_lesson.get(
            "title",
            lesson_name.replace("_", " ").title()
        ),

        "lesson_icon": localized_lesson.get(
            "icon",
            "📘"
        ),

        "lesson_description": localized_lesson.get(
            "description",
            ""
        ),

        "skill": recommendation.get(
            "skill",
            "Learning"
        ),

        "learner_level": predicted_level,

        "proficiency_score": proficiency["score"],

        "reason": recommendation.get(
            "reason",
            ""
        ),

        "questions": selected_questions,

        "total_questions": len(
            selected_questions
        )
    }
# =========================================================
# PERSONALIZED LESSON
# =========================================================

@app.route("/personalized-lesson")
def personalized_lesson():

    # -----------------------------------------------------
    # Check login
    # -----------------------------------------------------

    if "user_id" not in session:

        return redirect("/login")


    # -----------------------------------------------------
    # Generate personalized lesson
    # -----------------------------------------------------

    personalized_lesson = generate_personalized_lesson(
        session["user_id"]
    )


    # -----------------------------------------------------
    # Safety check
    # -----------------------------------------------------

    if personalized_lesson is None:

        return redirect("/learn")


    # -----------------------------------------------------
    # Send personalized lesson to HTML
    # -----------------------------------------------------

    return render_template(
        "personalized_lesson.html",
        personalized_lesson=personalized_lesson
    )
# =========================================================
# MILESTONE 2 - LEARNING PATH MANAGEMENT
# =========================================================

def create_learning_path(user_id):
    """
    Create a personalized learning path for the learner.

    Priority:
    1. Current adaptive recommendation
    2. Uncompleted lessons
    3. Completed lessons for revision
    """

    connection = get_db_connection()

    # -----------------------------------------------------
    # Lesson order
    # -----------------------------------------------------

    lesson_order = [
        "alphabet",
        "sounds",
        "alphabet_examples",
        "basic_words",
        "family_words",
        "food_words",
        "colors",
        "numbers",
        "animals",
        "simple_sentences"
    ]

    # -----------------------------------------------------
    # Get completed lessons
    # -----------------------------------------------------

    completed_rows = connection.execute(
        """
        SELECT lesson, completed, best_score
        FROM lesson_progress
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchall()

    completed = {
        row["lesson"]: row
        for row in completed_rows
    }

    connection.close()

    # -----------------------------------------------------
    # Get adaptive recommendation
    # -----------------------------------------------------

    recommendation = get_adaptive_recommendation(user_id)

    recommended_lesson = recommendation.get(
        "lesson_name"
    )

    # -----------------------------------------------------
    # Build personalized order
    # -----------------------------------------------------

    ordered_lessons = []

    # First: adaptive recommendation
    if (
        recommended_lesson
        and recommended_lesson in lesson_order
    ):
        ordered_lessons.append(
            recommended_lesson
        )

    # Second: uncompleted lessons
    for lesson_name in lesson_order:

        if lesson_name in ordered_lessons:
            continue

        if (
            lesson_name not in completed
            or not completed[lesson_name]["completed"]
        ):
            ordered_lessons.append(
                lesson_name
            )

    # Third: completed lessons for revision
    for lesson_name in lesson_order:

        if lesson_name not in ordered_lessons:
            ordered_lessons.append(
                lesson_name
            )

    # -----------------------------------------------------
    # Save path
    # -----------------------------------------------------

    connection = get_db_connection()

    # Rebuild current path
    connection.execute(
        """
        DELETE FROM learning_paths
        WHERE user_id = ?
        """,
        (user_id,)
    )

    for position, lesson_name in enumerate(
        ordered_lessons,
        start=1
    ):

        lesson_row = completed.get(
            lesson_name
        )

        if lesson_row:

            if lesson_row["completed"]:
                status = "completed"
            else:
                status = "not_started"

            score = lesson_row["best_score"] or 0

        else:

            status = "not_started"
            score = 0

        connection.execute(
            """
            INSERT INTO learning_paths
            (
                user_id,
                lesson,
                position,
                status,
                score
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user_id,
                lesson_name,
                position,
                status,
                score
            )
        )

    connection.commit()
    connection.close()

    return ordered_lessons


# =========================================================
# GET /api/learning-path
# =========================================================

@app.route(
    "/api/learning-path",
    methods=["GET"]
)
def api_get_learning_path():

    if "user_id" not in session:

        return jsonify({
            "success": False,
            "message": "Please login first."
        }), 401

    user_id = session["user_id"]

    # Create/rebuild path
    create_learning_path(user_id)

    connection = get_db_connection()

    rows = connection.execute(
        """
        SELECT
            lesson,
            position,
            status,
            score
        FROM learning_paths
        WHERE user_id = ?
        ORDER BY position
        """,
        (user_id,)
    ).fetchall()

    connection.close()

    # Get localized lesson data
    localized_lessons = get_localized_lessons()

    learning_path = []

    for row in rows:

        lesson_name = row["lesson"]

        lesson = localized_lessons.get(
            lesson_name,
            {}
        )

        learning_path.append({

            "lesson": lesson_name,

            "title": lesson.get(
                "title",
                lesson_name.replace(
                    "_",
                    " "
                ).title()
            ),

            "description": lesson.get(
                "description",
                ""
            ),

            "position": row["position"],

            "status": row["status"],

            "score": row["score"]
        })

    return jsonify({

        "success": True,

        "preferred_language":
            get_current_language(),

        "learning_language":
            get_learning_language(),

        "total_lessons":
            len(learning_path),

        "learning_path":
            learning_path
    })

# =========================================================
# POST /api/learning-path
# =========================================================

@app.route(
    "/api/learning-path",
    methods=["POST"]
)
def api_create_learning_path():

    if "user_id" not in session:

        return jsonify({
            "success": False,
            "message": "Please login first."
        }), 401

    user_id = session["user_id"]

    create_learning_path(user_id)

    return jsonify({

        "success": True,

        "message":
            "Personalized learning path created successfully.",

        "learning_path_url":
            "/api/learning-path",

        "progress_url":
            "/api/learning-path/progress"
    }), 
# =========================================================
# GET /api/learning-path/progress
# =========================================================

@app.route(
    "/api/learning-path/progress",
    methods=["GET"]
)
def api_learning_path_progress():

    if "user_id" not in session:

        return jsonify({
            "success": False,
            "message": "Please login first."
        }), 401

    user_id = session["user_id"]

    connection = get_db_connection()

    rows = connection.execute(
        """
        SELECT
            lesson,
            position,
            status,
            score
        FROM learning_paths
        WHERE user_id = ?
        ORDER BY position
        """,
        (user_id,)
    ).fetchall()

    connection.close()

    total = len(rows)

    completed = sum(
        1
        for row in rows
        if row["status"] == "completed"
    )

    if total > 0:
        percentage = round(
            (completed / total) * 100
        )
    else:
        percentage = 0

    return jsonify({

        "success": True,

        "total_lessons": total,

        "completed_lessons":
            completed,

        "remaining_lessons":
            total - completed,

        "progress_percentage":
            percentage
    })
# =========================================================
# PUT /api/learning-path/<lesson_name>
# =========================================================

@app.route(
    "/api/learning-path/<lesson_name>",
    methods=["PUT"]
)
def api_update_learning_path_lesson(
    lesson_name
):

    if "user_id" not in session:

        return jsonify({
            "success": False,
            "message": "Please login first."
        }), 401

    user_id = session["user_id"]

    data = request.get_json(
        silent=True
    ) or {}

    status = data.get(
        "status",
        "not_started"
    )

    score = data.get(
        "score",
        0
    )

    allowed_statuses = [
        "not_started",
        "in_progress",
        "completed"
    ]

    if status not in allowed_statuses:

        return jsonify({

            "success": False,

            "message":
                "Invalid status. Use not_started, in_progress or completed."
        }), 400

    connection = get_db_connection()

    existing = connection.execute(
        """
        SELECT *
        FROM learning_paths
        WHERE user_id = ?
        AND lesson = ?
        """,
        (
            user_id,
            lesson_name
        )
    ).fetchone()

    if not existing:

        connection.close()

        return jsonify({

            "success": False,

            "message":
                "Lesson is not present in the learning path."
        }), 404

    connection.execute(
        """
        UPDATE learning_paths

        SET status = ?,
            score = ?,
            updated_at = CURRENT_TIMESTAMP

        WHERE user_id = ?
        AND lesson = ?
        """,
        (
            status,
            score,
            user_id,
            lesson_name
        )
    )

    connection.commit()
    connection.close()

    return jsonify({

        "success": True,

        "message":
            "Learning path updated successfully.",

        "lesson":
            lesson_name,

        "status":
            status,

        "score":
            score
    })

@app.route("/dashboard")
def dashboard():

    # -----------------------------------------------------
    # CHECK LOGIN
    # -----------------------------------------------------

    if "user_id" not in session:
        return redirect("/login")
            # -----------------------------------------------------
    # CHECK INITIAL ASSESSMENT
    # -----------------------------------------------------

    # -----------------------------------------------------
    # DATABASE
    # -----------------------------------------------------

    connection = get_db_connection()

     # =====================================================
    # MILESTONE 2 - LEARNER SKILL ANALYSIS
    # =====================================================

    skill_performance = connection.execute(
        """
        SELECT lsp.skill,
               lsp.correct_answers,
               lsp.total_answers,
               lsp.proficiency_score,
               lsp.proficiency_level
        FROM learner_skill_performance AS lsp
        INNER JOIN (
            SELECT skill, MAX(id) AS latest_id
            FROM learner_skill_performance
            WHERE user_id = ?
            GROUP BY skill
        ) AS latest
            ON lsp.skill = latest.skill
           AND lsp.id = latest.latest_id
        WHERE lsp.user_id = ?
        ORDER BY lsp.id DESC
        """,
        (
            session["user_id"],
            session["user_id"],
        )
    ).fetchall()


    # =====================================================
    # MILESTONE 2 - WEAK / STRONG SKILL DETECTION
    # =====================================================

    weak_skills = []
    developing_skills = []
    strong_skills = []

    for skill in skill_performance:

        score = skill["proficiency_score"]

        if score < 60:

            weak_skills.append(skill)

        elif score < 80:

            developing_skills.append(skill)

        else:

            strong_skills.append(skill)


    # -----------------------------------------------------
    # GET USER
    # -----------------------------------------------------

    user = connection.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    # -----------------------------------------------------
    # GET PROGRESS
    # -----------------------------------------------------

    progress = connection.execute(
        """
        SELECT *
        FROM user_progress
        WHERE user_id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    # -----------------------------------------------------
    # GET COMPLETED LESSONS
    # -----------------------------------------------------

    completed_lessons = connection.execute(
        """
        SELECT COUNT(*)
        FROM lesson_progress
        WHERE user_id = ?
        AND completed = 1
        """,
        (
            session["user_id"],
        )
    ).fetchone()[0]


    # -----------------------------------------------------
    # GET TOTAL LESSONS
    # -----------------------------------------------------

    total_lessons = len(LESSONS)


    # -----------------------------------------------------
    # OVERALL PROGRESS
    # -----------------------------------------------------

    if progress:

        overall_progress = round(
            (
                progress["reading_progress"]
                +
                progress["writing_progress"]
                +
                progress["speaking_progress"]
            ) / 3
        )

    else:

        overall_progress = 0


    # =====================================================
    # MILESTONE 2 - ADAPTIVE LEARNING RECOMMENDATION
    # =====================================================

    adaptive_recommendation = get_adaptive_recommendation(
        session["user_id"]
    )
    learning_path_levels = get_learning_path_levels(
    session["user_id"]
)
    preferred_language = get_current_language()
    learning_path_text = LEARNING_PATH_TRANSLATIONS.get(
    preferred_language,
    LEARNING_PATH_TRANSLATIONS["English"]
)
    content_recommendations = get_content_recommendations(
    session["user_id"]
)
    proficiency_prediction = predict_learner_proficiency(
    session["user_id"]
)

 


    # -----------------------------------------------------
    # CLOSE DATABASE
    # -----------------------------------------------------

    connection.close()


    # -----------------------------------------------------
    # SEND DATA TO DASHBOARD
    # -----------------------------------------------------
    return render_template(
        "dashboard.html",
        user=user,
        progress=progress,
        overall_progress=overall_progress,
        completed_lessons=completed_lessons,
        total_lessons=total_lessons,
        skill_performance=skill_performance,
        weak_skills=weak_skills,
        developing_skills=developing_skills,
        strong_skills=strong_skills,
        adaptive_recommendation=adaptive_recommendation,
        content_recommendations=content_recommendations,
        learning_path_levels=learning_path_levels,
        learning_path_text=learning_path_text
    )

# =========================================================
# LEARN
# =========================================================

@app.route("/learn")
def learn():

    if "user_id" not in session:

        return redirect("/login")


    connection = get_db_connection()


    user = connection.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    progress = connection.execute(
        """
        SELECT *
        FROM user_progress
        WHERE user_id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    lesson_progress = connection.execute(
        """
        SELECT *
        FROM lesson_progress
        WHERE user_id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchall()


    connection.close()


    return render_template(
        "learn.html",
        user=user,
        progress=progress,
        lesson_progress=lesson_progress,
        lessons=get_localized_lessons(),
        game_data=get_learning_game_data()
    )


# =========================================================
# ACTUAL DYNAMIC LESSON ROUTE
#
# IMPORTANT:
# LESSONS = {...} IS ABOVE THIS ROUTE.
# =========================================================

@app.route(
    "/lesson/<lesson_name>",
    methods=["GET", "POST"]
)
def lesson(lesson_name):

    # -----------------------------------------------------
    # Check login
    # -----------------------------------------------------

    if "user_id" not in session:

        return redirect("/login")


    # -----------------------------------------------------
    # Check lesson exists
    # -----------------------------------------------------

    if lesson_name not in LESSONS:

        return redirect("/learn")

    
    lesson_data = get_localized_lessons().get(
        lesson_name,
        LESSONS[lesson_name]
    )
    questions = lesson_data.get(
        "questions",
        []
    )


    

    total_questions = len(questions)

    localized_lessons = get_localized_lessons()
    lesson_data = localized_lessons[lesson_name]
    questions = lesson_data["questions"]


    # -----------------------------------------------------
    # START / RESTART LESSON
    # -----------------------------------------------------

    if request.args.get("restart") == "1":

        session["current_lesson"] = lesson_name

        session["lesson_question"] = 0

        session["lesson_score"] = 0

        session.pop("last_answer_index", None)


    elif request.method == "GET":

        if session.get("current_lesson") != lesson_name:

            session["current_lesson"] = lesson_name

            session["lesson_question"] = 0

            session["lesson_score"] = 0

            session.pop("last_answer_index", None)


    # -----------------------------------------------------
    # CURRENT QUESTION INDEX
    # -----------------------------------------------------

    question_index = session.get(
        "lesson_question",
        0
    )

    score = session.get(
        "lesson_score",
        0
    )


    # -----------------------------------------------------
    # SAFETY CHECK
    # -----------------------------------------------------

    if question_index >= total_questions:

        return redirect(
            url_for(
                "lesson_complete",
                lesson_name=lesson_name
            )
        )


    # -----------------------------------------------------
    # POST ANSWER
    # -----------------------------------------------------

    if request.method == "POST":

        # Prevent duplicate submission
        if session.get("last_answer_index") == question_index:

            return redirect(
                url_for(
                    "lesson",
                    lesson_name=lesson_name
                )
            )


        answer = request.form.get(
            "answer",
            ""
        ).strip()


        current_question = questions[
            question_index
        ]


        correct_answer = current_question[
            "answer"
        ]


        # Case-insensitive comparison
        is_correct = (
            answer.lower()
            ==
            correct_answer.lower()
        )


        xp_earned = 0


        if is_correct:

            score += 1

            xp_earned = 10

            message = "🎉 Correct! Great job!"


            # Add XP
            connection = get_db_connection()

            connection.execute(
                """
                UPDATE users
                SET xp = xp + ?
                WHERE id = ?
                """,
                (
                    xp_earned,
                    session["user_id"]
                )
            )

            connection.commit()

            connection.close()


            update_user_level(
                session["user_id"]
            )


        else:

            message = (
                "❌ Not quite. "
                "The correct answer is: "
                + correct_answer
            )


        # Save score
        session["lesson_score"] = score

        session["last_answer_index"] = question_index

        session["lesson_question"] = (
            question_index + 1
        )


        # -------------------------------------------------
        # IF THIS WAS THE LAST QUESTION
        # -------------------------------------------------

        if question_index + 1 >= total_questions:
            return redirect(url_for(
            "lesson_complete",
            lesson_name=lesson_name
        )
    )


# -------------------------------------------------
# SHOW FEEDBACK
# -------------------------------------------------

            # -----------------------------------------------------

        return render_template(
            "lesson_feedback.html",

            lesson_name=lesson_name,
            lesson_title=lesson_data["title"],
            lesson_icon=lesson_data["icon"],

            question=current_question,

            message=message,

            explanation=current_question.get(
                "help",
                ""
            ),

            xp_earned=xp_earned,
            is_correct=is_correct,

            score=score,

            question_number=question_index + 1,

            total_questions=total_questions
        )

    # -----------------------------------------------------
    # DISPLAY CURRENT QUESTION
    # -----------------------------------------------------

    current_question = questions[
        question_index
    ]

    progress_percent = int(
        (
            question_index
            /
            total_questions
        ) * 100
    )

    return render_template(
        "lesson.html",

        lesson_name=lesson_name,

        lesson_title=lesson_data["title"],

        lesson_icon=lesson_data["icon"],

        lesson_description=
            lesson_data["description"],

        question=current_question[
            "question"
        ],

        options=current_question[
            "options"
        ],

        help_text=current_question.get(
            "help",
            ""
        ),

        question_number=
            question_index + 1,

        total_questions=
            total_questions,

        progress_percent=
            progress_percent,

        xp=score * 10,

        score=score
    )

# =========================================================
# LESSON COMPLETE
# =========================================================
# =========================================================
# LESSON COMPLETE
# =========================================================

@app.route("/lesson/<lesson_name>/complete")
def lesson_complete(lesson_name):

    # -----------------------------------------------------
    # CHECK LOGIN
    # -----------------------------------------------------

    if "user_id" not in session:
        return redirect("/login")
            # -----------------------------------------------------
    # CHECK INITIAL ASSESSMENT
    # -----------------------------------------------------

    assessment_connection = get_db_connection()

    assessment_done = assessment_connection.execute(
        """
        SELECT COUNT(*)
        FROM assessment_attempts
        WHERE user_id = ?
        """,
        (session["user_id"],)
    ).fetchone()[0]

    assessment_connection.close()

    if assessment_done == 0:
        return redirect("/assessment")


    # -----------------------------------------------------
    # CHECK LESSON
    # -----------------------------------------------------

    if lesson_name not in LESSONS:
        return redirect("/learn")


    lesson_data = LESSONS[lesson_name]

    total_questions = len(
        lesson_data["questions"]
    )


    # -----------------------------------------------------
    # GET SCORE
    # -----------------------------------------------------

    score = session.get(
        "lesson_score",
        0
    )


    if total_questions > 0:

        percentage = round(
            (
                score /
                total_questions
            ) * 100
        )

    else:

        percentage = 0


    # -----------------------------------------------------
    # DATABASE
    # -----------------------------------------------------

    connection = get_db_connection()


    # =====================================================
    # 1. SAVE / UPDATE LESSON PROGRESS
    # =====================================================

    existing_lesson = connection.execute(
        """
        SELECT *
        FROM lesson_progress
        WHERE user_id = ?
        AND lesson = ?
        """,
        (
            session["user_id"],
            lesson_name
        )
    ).fetchone()


    if existing_lesson:

        # Update existing lesson instead of
        # creating duplicate rows.

        connection.execute(
            """
            UPDATE lesson_progress

            SET
                completed = 1,

                best_score =
                    CASE
                        WHEN best_score < ?
                        THEN ?
                        ELSE best_score
                    END,

                total_questions = ?,

                attempts = attempts + 1,

                last_attempt =
                    CURRENT_TIMESTAMP

            WHERE user_id = ?

            AND lesson = ?
            """,
            (
                score,
                score,
                total_questions,
                session["user_id"],
                lesson_name
            )
        )

    else:

        # First attempt

        connection.execute(
            """
            INSERT INTO lesson_progress
            (
                user_id,
                lesson,
                completed,
                best_score,
                total_questions,
                attempts
            )

            VALUES
            (
                ?,
                ?,
                1,
                ?,
                ?,
                1
            )
            """,
            (
                session["user_id"],
                lesson_name,
                score,
                total_questions
            )
        )


    # =====================================================
    # 2. UPDATE READING PROGRESS
    # =====================================================

    reading_lessons = [
        "alphabet",
        "sounds",
        "alphabet_examples",
        "basic_words",
        "family_words",
        "food_words",
        "colors",
        "numbers",
        "animals"
    ]


    if lesson_name in reading_lessons:

        connection.execute(
            """
            UPDATE user_progress

            SET reading_progress =
                MIN(
                    reading_progress + 10,
                    100
                )

            WHERE user_id = ?
            """,
            (
                session["user_id"],
            )
        )


    # =====================================================
    # 3. UPDATE WRITING PROGRESS
    # =====================================================

    elif lesson_name == "simple_sentences":

        connection.execute(
            """
            UPDATE user_progress

            SET writing_progress =
                MIN(
                    writing_progress + 10,
                    100
                )

            WHERE user_id = ?
            """,
            (
                session["user_id"],
            )
        )


    # =====================================================
    # 4. SAVE DATABASE
    # =====================================================

    connection.commit()


    # =====================================================
    # 5. GET UPDATED USER
    # =====================================================

    user = connection.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    connection.close()


    # =====================================================
    # 6. UPDATE LEVEL
    # =====================================================

    update_user_level(
        session["user_id"]
    )


    # =====================================================
    # 7. CLEAR TEMPORARY SESSION DATA
    # =====================================================

    session.pop(
        "lesson_question",
        None
    )

    session.pop(
        "lesson_score",
        None
    )

    session.pop(
        "last_answer_index",
        None
    )


    # =====================================================
    # 8. SHOW COMPLETION PAGE
    # =====================================================

    return render_template(
        "lesson_complete.html",

        lesson_name=lesson_name,

        lesson_title=
            lesson_data["title"],

        lesson_icon=
            lesson_data["icon"],

        score=score,

        total=total_questions,

        percentage=percentage,

        xp=score * 10
    )
# =========================================================
# READING PRACTICE
#
# OLD /reading URL NOW REDIRECTS TO ALPHABET
# =========================================================

@app.route("/reading")
def reading():

    if "user_id" not in session:

        return redirect("/login")


    return redirect(
        url_for(
            "lesson",
            lesson_name="alphabet"
        )
    )


# =========================================================
# WRITING PRACTICE
#
# OLD /writing URL NOW REDIRECTS TO SENTENCES
# =========================================================

@app.route("/writing")
def writing():

    if "user_id" not in session:

        return redirect("/login")


    return redirect(
        url_for(
            "lesson",
            lesson_name="simple_sentences"
        )
    )


# =========================================================
# VOICE PRACTICE
# =========================================================


# =========================================================
# VOICE PRACTICE
# =========================================================

@app.route("/voice")
def voice():

    if "user_id" not in session:
        return redirect("/login")


    # -----------------------------------------------------
    # Database connection
    # -----------------------------------------------------

    connection = get_db_connection()


    user = connection.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    connection.close()


    # -----------------------------------------------------
    # Keep interface language and learning language separate
    # -----------------------------------------------------

    preferred_language = user["preferred_language"] or "English"
    learning_language = user["learning_language"] or "English"


    # -----------------------------------------------------
    # Multiple speaking sentences
    # -----------------------------------------------------

    voice_sentences = {

        "English": [

            "Hello, how are you?",

            "My name is Archana.",

            "I am learning English.",

            "I like reading books.",

            "I go to college every day.",

            "Today is a beautiful day.",

            "I want to improve my speaking skills.",

            "Learning new words is interesting.",

            "I enjoy spending time with my friends.",

            "I am confident that I can learn."
        ],


        "Telugu": [

            "మీరు ఎలా ఉన్నారు?",

            "నా పేరు అర్చన.",

            "నేను ఇంగ్లీష్ నేర్చుకుంటున్నాను.",

            "నాకు పుస్తకాలు చదవడం ఇష్టం.",

            "నేను ప్రతిరోజూ కాలేజీకి వెళ్తాను.",

            "ఈ రోజు చాలా అందమైన రోజు.",

            "నా మాట్లాడే నైపుణ్యాలను మెరుగుపరచుకోవాలనుకుంటున్నాను.",

            "కొత్త పదాలను నేర్చుకోవడం ఆసక్తికరంగా ఉంటుంది.",

            "నా స్నేహితులతో సమయం గడపడం నాకు ఇష్టం.",

            "నేను నేర్చుకోగలననే నమ్మకం నాకు ఉంది."
        ],


        "Hindi": [

            "आप कैसे हैं?",

            "मेरा नाम अर्चना है।",

            "मैं अंग्रेजी सीख रही हूँ।",

            "मुझे किताबें पढ़ना पसंद है।",

            "मैं हर दिन कॉलेज जाती हूँ।",

            "आज एक सुंदर दिन है।",

            "मैं अपने बोलने के कौशल को सुधारना चाहती हूँ।",

            "नए शब्द सीखना दिलचस्प है।",

            "मुझे अपने दोस्तों के साथ समय बिताना पसंद है।",

            "मुझे विश्वास है कि मैं सीख सकती हूँ।"
        ]

    }


    # -----------------------------------------------------
    # Select sentences for language
    # -----------------------------------------------------

    sentences = voice_sentences.get(
        learning_language,
        voice_sentences["English"]
    )


    # -----------------------------------------------------
    # Browser speech recognition language
    # -----------------------------------------------------

    speech_languages = {

        "English": "en-IN",

        "Telugu": "te-IN",

        "Hindi": "hi-IN"

    }


    speech_language = speech_languages.get(
        learning_language,
        "en-IN"
    )


    # -----------------------------------------------------
    # Send data to HTML
    # -----------------------------------------------------

    return render_template(
        "voice.html",

        user=user,

        sentences=sentences,

        speech_language=speech_language,

        preferred_language=preferred_language,

        learning_language=learning_language
    )

# =========================================================
# SPEAKING
# =========================================================

# =========================================================
# SPEAKING
# =========================================================

@app.route("/speaking")
def speaking():

    if "user_id" not in session:
        return redirect("/login")

    return redirect("/voice")


# =========================================================
# COMPLETE VOICE PRACTICE
# =========================================================

# =========================================================
# COMPLETE VOICE PRACTICE
# =========================================================

@app.route(
    "/voice/complete",
    methods=["POST"]
)
def voice_complete():

    # -----------------------------------------------------
    # CHECK LOGIN
    # -----------------------------------------------------

    if "user_id" not in session:

        return {
            "success": False,
            "message": "Please login first."
        }, 401


    # -----------------------------------------------------
    # DATABASE
    # -----------------------------------------------------

    connection = get_db_connection()


    # =====================================================
    # 1. UPDATE SPEAKING PROGRESS
    # =====================================================

    connection.execute(
        """
        UPDATE user_progress

        SET speaking_progress =
            MIN(
                speaking_progress + 10,
                100
            )

        WHERE user_id = ?
        """,
        (
            session["user_id"],
        )
    )


    # =====================================================
    # 2. ADD XP
    # =====================================================

    connection.execute(
        """
        UPDATE users

        SET xp = xp + 10

        WHERE id = ?
        """,
        (
            session["user_id"],
        )
    )


    # =====================================================
    # 3. GET UPDATED USER
    # =====================================================

    user = connection.execute(
        """
        SELECT
            xp,
            streak,
            level

        FROM users

        WHERE id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    # =====================================================
    # 4. SAVE
    # =====================================================

    connection.commit()

    connection.close()


    # =====================================================
    # 5. UPDATE LEVEL
    # =====================================================

    update_user_level(
        session["user_id"]
    )


    # =====================================================
    # 6. RETURN RESULT
    # =====================================================

    return {
        "success": True,

        "xp": 10,

        "total_xp": user["xp"],

        "streak": user["streak"],

        "level": user["level"]
    }
# =========================================================
# PROGRESS
# =========================================================
# =========================================================
# PROGRESS
# =========================================================

@app.route("/progress")
def progress():

    # -----------------------------------------------------
    # Check login
    # -----------------------------------------------------

    if "user_id" not in session:
        return redirect("/login")


    # -----------------------------------------------------
    # Database connection
    # -----------------------------------------------------

    connection = get_db_connection()


    # -----------------------------------------------------
    # Get user
    # -----------------------------------------------------

    user = connection.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    # -----------------------------------------------------
    # Get skill progress
    # -----------------------------------------------------

    progress_data = connection.execute(
        """
        SELECT *
        FROM user_progress
        WHERE user_id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    # -----------------------------------------------------
    # Get lesson progress
    # -----------------------------------------------------

    lesson_progress = connection.execute(
        """
        SELECT *
        FROM lesson_progress
        WHERE user_id = ?
        ORDER BY id
        """,
        (
            session["user_id"],
        )
    ).fetchall()


    connection.close()


    # -----------------------------------------------------
    # Safety: if progress row doesn't exist
    # -----------------------------------------------------

    if progress_data is None:

        reading_progress = 0
        writing_progress = 0
        speaking_progress = 0

    else:

        reading_progress = progress_data["reading_progress"]
        writing_progress = progress_data["writing_progress"]
        speaking_progress = progress_data["speaking_progress"]


    # -----------------------------------------------------
    # Overall progress
    # -----------------------------------------------------

    overall_progress = round(
        (
            reading_progress
            +
            writing_progress
            +
            speaking_progress
        )
        / 3
    )


    # -----------------------------------------------------
    # Make sure progress stays between 0 and 100
    # -----------------------------------------------------

    overall_progress = max(
        0,
        min(
            overall_progress,
            100
        )
    )


    # -----------------------------------------------------
    # Render progress page
    # -----------------------------------------------------

    return render_template(
        "progress.html",

        user=user,

        progress=progress_data,

        lesson_progress=lesson_progress,

        overall_progress=overall_progress
    )
# =========================================================
# STEP 5 - LEARNING REPORT
# =========================================================
# =========================================================
# GENERATE LEARNING REPORT
# =========================================================

def generate_learning_report(user_id):

    connection = get_db_connection()

    # -----------------------------------------------------
    # GET USER INFORMATION
    # -----------------------------------------------------

    user = connection.execute(
        """
        SELECT
            name,
            xp,
            streak,
            level
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    ).fetchone()


    # -----------------------------------------------------
    # GET READING / WRITING / SPEAKING PROGRESS
    # -----------------------------------------------------

    progress = connection.execute(
        """
        SELECT
            reading_progress,
            writing_progress,
            speaking_progress
        FROM user_progress
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchone()


    # -----------------------------------------------------
    # GET COMPLETED LESSON COUNT
    # -----------------------------------------------------

    completed_lessons = connection.execute(
        """
        SELECT COUNT(*) AS total
        FROM lesson_progress
        WHERE user_id = ?
        AND completed = 1
        """,
        (user_id,)
    ).fetchone()


    # -----------------------------------------------------
    # GET LATEST SKILL PERFORMANCE
    # -----------------------------------------------------

    skill_rows = connection.execute(
        """
        SELECT
            lsp.skill,
            lsp.proficiency_score,
            lsp.proficiency_level
        FROM learner_skill_performance AS lsp

        INNER JOIN (
            SELECT
                skill,
                MAX(id) AS latest_id
            FROM learner_skill_performance
            WHERE user_id = ?
            GROUP BY skill
        ) AS latest

        ON lsp.skill = latest.skill
        AND lsp.id = latest.latest_id

        WHERE lsp.user_id = ?
        """,
        (
            user_id,
            user_id
        )
    ).fetchall()


    connection.close()


    # -----------------------------------------------------
    # SAFETY VALUES
    # -----------------------------------------------------

    if user is None:
        return {}


    if progress is None:

        reading = 0
        writing = 0
        speaking = 0

    else:

        reading = progress["reading_progress"] or 0
        writing = progress["writing_progress"] or 0
        speaking = progress["speaking_progress"] or 0


    # -----------------------------------------------------
    # OVERALL PROGRESS
    # -----------------------------------------------------

    overall = round(
        (
            reading +
            writing +
            speaking
        ) / 3
    )


    # -----------------------------------------------------
    # SKILL CLASSIFICATION
    # -----------------------------------------------------

    weak_skills = []
    developing_skills = []
    strong_skills = []


    for row in skill_rows:

        skill = row["skill"]

        try:
            score = float(
                row["proficiency_score"] or 0
            )
        except (TypeError, ValueError):
            score = 0


        if score < 60:

            weak_skills.append(skill)

        elif score < 80:

            developing_skills.append(skill)

        else:

            strong_skills.append(skill)


    # -----------------------------------------------------
    # IMPROVEMENT RECOMMENDATIONS
    # -----------------------------------------------------

    recommendations = []


    if reading < 60:

        recommendations.append(
            "Practice reading lessons regularly "
            "to improve reading skills."
        )


    if writing < 60:

        recommendations.append(
            "Practice writing exercises "
            "to improve writing skills."
        )


    if speaking < 60:

        recommendations.append(
            "Practice speaking and pronunciation "
            "regularly using Voice Practice."
        )


    if weak_skills:

        recommendations.append(
            "Focus more practice on: "
            + ", ".join(weak_skills)
        )


    if not recommendations:

        recommendations.append(
            "Continue practicing regularly "
            "to maintain your learning progress."
        )


    # -----------------------------------------------------
    # FINAL REPORT
    # -----------------------------------------------------

    report = {

        "learner_name":
            user["name"],

        "xp":
            user["xp"] or 0,

        "level":
            user["level"] or 1,

        "streak":
            user["streak"] or 0,

        "reading":
            reading,

        "writing":
            writing,

        "speaking":
            speaking,

        "overall":
            overall,

        "completed_lessons":
            completed_lessons["total"] or 0,

        "weak_skills":
            weak_skills,

        "developing_skills":
            developing_skills,

        "strong_skills":
            strong_skills,

        "recommendations":
            recommendations
    }


    return report

# =========================================================
# LEARNING REPORT PAGE
# =========================================================

@app.route("/learning-report")
def learning_report():

    # -----------------------------------------------------
    # CHECK LOGIN
    # -----------------------------------------------------

    if "user_id" not in session:

        return redirect("/login")


    # -----------------------------------------------------
    # GENERATE REPORT
    # -----------------------------------------------------

    report = generate_learning_report(
        session["user_id"]
    )


    # -----------------------------------------------------
    # SEND REPORT TO HTML
    # -----------------------------------------------------

    return render_template(
        "learning_report.html",
        report=report
    )

# =========================================================
# PROFILE
# =========================================================

@app.route("/profile")
def profile():

    if "user_id" not in session:

        return redirect("/login")


    connection = get_db_connection()


    user = connection.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (
            session["user_id"],
        )
    ).fetchone()


    connection.close()


    return render_template(
        "profile.html",
        user=user
    )


# =========================================================
# INITIAL ASSESSMENT - PERSONALIZED LEARNING GUIDANCE
# =========================================================

def get_initial_assessment_guidance(user_id):
    """
    Analyze the learner's latest initial assessment and decide:

    1. Which skills need improvement
    2. Which lesson should be learned first
    3. Which lessons should be learned next
    4. Why those lessons are recommended
    """

    connection = get_db_connection()

    # -----------------------------------------------------
    # GET LATEST ASSESSMENT PERFORMANCE FOR EACH SKILL
    # -----------------------------------------------------

    skill_rows = connection.execute(
        """
        SELECT skill,
               correct_answers,
               total_answers,
               proficiency_score,
               proficiency_level
        FROM learner_skill_performance
        WHERE user_id = ?
        AND skill IN (
            'Reading',
            'Writing',
            'Comprehension'
        )
        AND id IN (
            SELECT MAX(id)
            FROM learner_skill_performance
            WHERE user_id = ?
            AND skill IN (
                'Reading',
                'Writing',
                'Comprehension'
            )
            GROUP BY skill
        )
        ORDER BY proficiency_score ASC
        """,
        (
            user_id,
            user_id
        )
    ).fetchall()

    connection.close()

    # -----------------------------------------------------
    # LESSONS CONNECTED TO EACH ASSESSMENT SKILL
    # -----------------------------------------------------

    skill_to_lessons = {

        "Reading": [
            "alphabet",
            "sounds",
            "alphabet_examples",
            "basic_words"
        ],

        "Writing": [
            "alphabet_examples",
            "basic_words",
            "simple_sentences"
        ],

        "Comprehension": [
            "basic_words",
            "family_words",
            "food_words",
            "simple_sentences"
        ]
    }

    # -----------------------------------------------------
    # GET LOCALIZED LESSON INFORMATION
    # -----------------------------------------------------

    localized_lessons = get_localized_lessons()

    # -----------------------------------------------------
    # STORE SKILL IMPROVEMENT INFORMATION
    # -----------------------------------------------------

    improvement_skills = []

    for row in skill_rows:

        try:
            score = round(
                float(row["proficiency_score"] or 0)
            )
        except (TypeError, ValueError):
            score = 0

        skill = row["skill"]

        level = (
            row["proficiency_level"]
            or "Beginner"
        )

        # ---------------------------------------------
        # DETERMINE IMPROVEMENT STATUS
        # ---------------------------------------------

        if score < 40:

            status = "Needs strong improvement"

            message = (
                f"Your {skill} score is {score}%. "
                "You should start with the basic lessons "
                "for this skill."
            )

        elif score < 60:

            status = "Needs improvement"

            message = (
                f"Your {skill} score is {score}%. "
                "More practice is recommended."
            )

        elif score < 80:

            status = "Developing"

            message = (
                f"Your {skill} score is {score}%. "
                "You are developing this skill. "
                "Continue practicing."
            )

        else:

            status = "Strong"

            message = (
                f"Your {skill} score is {score}%. "
                "This is currently one of your stronger skills."
            )

        improvement_skills.append(
            {
                "skill": skill,
                "score": score,
                "level": level,
                "status": status,
                "message": message
            }
        )

    # -----------------------------------------------------
    # FIND THE WEAKEST SKILL
    # -----------------------------------------------------

    if improvement_skills:

        weakest_skill_data = min(
            improvement_skills,
            key=lambda item: item["score"]
        )

        weakest_skill = weakest_skill_data["skill"]

        weakest_score = weakest_skill_data["score"]

        weakest_level = weakest_skill_data["level"]

    else:

        weakest_skill = "Reading"

        weakest_score = 0

        weakest_level = "Beginner"

    # -----------------------------------------------------
    # RECOMMEND LESSONS FOR THE WEAKEST SKILL
    # -----------------------------------------------------

    lesson_names = skill_to_lessons.get(
        weakest_skill,
        ["alphabet"]
    )

    recommended_lessons = []

    for lesson_name in lesson_names:

        lesson = localized_lessons.get(
            lesson_name,
            LESSONS.get(
                lesson_name,
                {}
            )
        )

        recommended_lessons.append(
            {
                "lesson_name": lesson_name,
                 "skill": weakest_skill,

                "lesson_title": lesson.get(
                    "title",
                    lesson_name.replace(
                        "_",
                        " "
                    ).title()
                ),

                "lesson_description": lesson.get(
                    "description",
                    ""
                ),

                "skill": weakest_skill,

                "score": weakest_score,

                "level": weakest_level
            }
        )

    # -----------------------------------------------------
    # SELECT FIRST LESSON
    # -----------------------------------------------------

    if recommended_lessons:

        next_lesson = recommended_lessons[0]

    else:

        next_lesson = {
            "lesson_name": "alphabet",
            "lesson_title": "Alphabet",
            "lesson_description":
                "Learn the basic letters and their sounds.",
            "skill": weakest_skill,
            "score": weakest_score,
            "level": weakest_level
        }

    # -----------------------------------------------------
    # CREATE OVERALL RECOMMENDATION MESSAGE
    # -----------------------------------------------------

    if weakest_score < 40:

        recommendation_message = (
            f"Your weakest area is {weakest_skill}. "
            f"Your score is {weakest_score}%. "
            "Start with the recommended basic lessons "
            "before moving to more advanced topics."
        )

    elif weakest_score < 60:

        recommendation_message = (
            f"Your {weakest_skill} skill needs improvement. "
            f"You scored {weakest_score}%. "
            "Practice the recommended lessons regularly."
        )

    elif weakest_score < 80:

        recommendation_message = (
            f"Your {weakest_skill} skill is developing. "
            f"You scored {weakest_score}%. "
            "Continue practicing these lessons to become stronger."
        )

    else:

        recommendation_message = (
            "Your assessment results are strong. "
            "Continue with the next lessons and gradually "
            "move toward more advanced learning."
        )

    # -----------------------------------------------------
    # RETURN COMPLETE GUIDANCE
    # -----------------------------------------------------

    return {
        "weakest_skill": weakest_skill,

        "weakest_score": weakest_score,

        "weakest_level": weakest_level,

        "improvement_skills":
            improvement_skills,

        "recommended_lessons":
            recommended_lessons,

        "next_lesson":
            next_lesson,

        "recommendation_message":
            recommendation_message
    }
# =========================================================
# INITIAL ASSESSMENT
# =========================================================
# =========================================================
# INITIAL ASSESSMENT GUIDANCE
# =========================================================

def get_initial_assessment_guidance(user_id):
    """
    Analyze the learner's latest initial assessment
    and recommend what the learner should improve
    and which lessons should be studied next.
    """

    connection = get_db_connection()

    # -----------------------------------------------------
    # GET LATEST ASSESSMENT SKILL PERFORMANCE
    # -----------------------------------------------------

    skill_rows = connection.execute(
        """
        SELECT skill,
               correct_answers,
               total_answers,
               proficiency_score,
               proficiency_level
        FROM learner_skill_performance
        WHERE user_id = ?
        AND id IN (
            SELECT MAX(id)
            FROM learner_skill_performance
            WHERE user_id = ?
            GROUP BY skill
        )
        """,
        (user_id, user_id)
    ).fetchall()

    connection.close()

    # -----------------------------------------------------
    # DEFAULT SKILL VALUES
    # -----------------------------------------------------

    skill_scores = {
        "Reading": 0,
        "Writing": 0,
        "Comprehension": 0
    }

    skill_levels = {
        "Reading": "Not Assessed",
        "Writing": "Not Assessed",
        "Comprehension": "Not Assessed"
    }

    # -----------------------------------------------------
    # STORE LATEST RESULTS
    # -----------------------------------------------------

    for row in skill_rows:

        skill = row["skill"]

        if skill in skill_scores:

            try:
                score = round(
                    float(row["proficiency_score"] or 0)
                )
            except (TypeError, ValueError):
                score = 0

            skill_scores[skill] = score

            skill_levels[skill] = (
                row["proficiency_level"]
                or "Beginner"
            )

    # -----------------------------------------------------
    # FIND WEAKEST SKILL
    # -----------------------------------------------------

    weakest_skill = min(
        skill_scores,
        key=skill_scores.get
    )

    weakest_score = skill_scores[weakest_skill]

    # -----------------------------------------------------
    # LESSON RECOMMENDATIONS
    # -----------------------------------------------------

    lesson_mapping = {

        "Reading": [
            "alphabet",
            "sounds",
            "alphabet_examples",
            "basic_words"
        ],

        "Writing": [
            "basic_words",
            "simple_sentences"
        ],

        "Comprehension": [
            "basic_words",
            "family_words",
            "food_words",
            "animals",
            "simple_sentences"
        ]
    }

    recommended_lessons = []

    for lesson_name in lesson_mapping.get(
        weakest_skill,
        []
    ):

        lesson = LESSONS.get(
            lesson_name,
            {}
        )

        recommended_lessons.append(
            {
                "name": lesson_name,

                "title": lesson.get(
                    "title",
                    lesson_name.replace(
                        "_",
                        " "
                    ).title()
                ),

                "icon": lesson.get(
                    "icon",
                    "📘"
                ),

                "description": lesson.get(
                    "description",
                    ""
                )
            }
        )

    # -----------------------------------------------------
    # LIMIT RECOMMENDATIONS
    # -----------------------------------------------------

    recommended_lessons = (
        recommended_lessons[:4]
    )

    # -----------------------------------------------------
    # IMPROVEMENT MESSAGE
    # -----------------------------------------------------

    if weakest_score < 40:

        improvement_message = (
            f"Your {weakest_skill} skill needs "
            f"strong improvement. "
            f"Your current score is {weakest_score}%. "
            f"Start with the recommended beginner "
            f"lessons below."
        )

    elif weakest_score < 60:

        improvement_message = (
            f"Your {weakest_skill} skill is at a "
            f"basic level with a score of "
            f"{weakest_score}%. "
            f"Practice the recommended lessons "
            f"to build a stronger foundation."
        )

    elif weakest_score < 80:

        improvement_message = (
            f"Your {weakest_skill} skill is developing "
            f"with a score of {weakest_score}%. "
            f"Continue practicing the recommended "
            f"lessons to reach a stronger level."
        )

    else:

        improvement_message = (
            f"Your {weakest_skill} skill is strong "
            f"with a score of {weakest_score}%. "
            f"Continue learning and move to the "
            f"next level."
        )

    # -----------------------------------------------------
    # NEXT LESSON
    # -----------------------------------------------------

    if recommended_lessons:

        next_lesson = recommended_lessons[0]

    else:

        next_lesson = {
            "name": "alphabet",
            "title": "Alphabet",
            "icon": "🔤",
            "description":
                "Learn the basic letters and their sounds."
        }

    # -----------------------------------------------------
    # OVERALL GUIDANCE
    # -----------------------------------------------------

    guidance = {

        "weakest_skill": weakest_skill,

        "weakest_score": weakest_score,

        "skill_scores": skill_scores,

        "skill_levels": skill_levels,

        "improvement_message":
            improvement_message,

        "recommended_lessons":
            recommended_lessons,

        "next_lesson":
            next_lesson
    }

    return guidance
@app.route(
    "/assessment",
    methods=["GET", "POST"]
)
def assessment():

    if "user_id" not in session:

        return redirect("/login")


    connection = get_db_connection()

# GET ASSESSMENT QUESTIONS
    learning_language = get_learning_language()
    questions = connection.execute(
    """
    SELECT *
    FROM assessment_questions
    WHERE language = ?
    ORDER BY id
    LIMIT 9
    """,
    (learning_language,)
    ).fetchall()


    connection.close()


    # -----------------------------------------------------
    # GET
    # -----------------------------------------------------

    if request.method == "GET":

        return render_template(
            "assessment.html",
            questions=questions,
            learning_language=learning_language
        )


    # -----------------------------------------------------
    # POST
    # -----------------------------------------------------

    score = 0

    total_questions = len(
        questions
    )

    answers = []


    for question in questions:

        question_id = question["id"]


        selected_answer = request.form.get(
            f"question_{question_id}",
            ""
        )


        correct_answer = (
            question["correct_answer"]
        )


        is_correct = (
            selected_answer.upper()
            ==
            correct_answer.upper()
        )


        if is_correct:

            score += 1


        answers.append(
            (
                question_id,
                selected_answer,
                1 if is_correct else 0
            )
        )


    # -----------------------------------------------------
    # Percentage
    # -----------------------------------------------------

    if total_questions > 0:

        percentage = (
            score
            /
            total_questions
        ) * 100

    else:

        percentage = 0


    # -----------------------------------------------------
    # Proficiency
    # -----------------------------------------------------

    if percentage < 40:

        proficiency_level = "Beginner"

    elif percentage < 75:

        proficiency_level = "Intermediate"

    else:

        proficiency_level = "Advanced"


    # -----------------------------------------------------
    # Save attempt
    # -----------------------------------------------------

    connection = get_db_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO assessment_attempts
        (
            user_id,
            score,
            total_questions,
            proficiency_level
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            session["user_id"],
            score,
            total_questions,
            proficiency_level
        )
    )


    attempt_id = cursor.lastrowid


    # -----------------------------------------------------
    # Save answers
    # -----------------------------------------------------

    for (
        question_id,
        selected_answer,
        is_correct
    ) in answers:

        cursor.execute(
            """
            INSERT INTO assessment_answers
            (
                attempt_id,
                question_id,
                selected_answer,
                is_correct
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                attempt_id,
                question_id,
                selected_answer,
                is_correct
            )
        )

    # -----------------------------------------------------
    # SAVE SKILL-WISE ASSESSMENT PERFORMANCE
    # -----------------------------------------------------

    skill_scores = {}

    for question_id, selected_answer, is_correct in answers:

        question = next(
            (
                q for q in questions
                if q["id"] == question_id
            ),
            None
        )

        if question is None:
            continue

        skill = question["skill"]

        if skill not in skill_scores:
            skill_scores[skill] = {
                "correct": 0,
                "total": 0
            }

        skill_scores[skill]["total"] += 1

        if is_correct:
            skill_scores[skill]["correct"] += 1


    # -----------------------------------------------------
    # INSERT SKILL PERFORMANCE
    # -----------------------------------------------------

    for skill, data in skill_scores.items():

        skill_total = data["total"]
        skill_correct = data["correct"]

        if skill_total > 0:

            skill_percentage = round(
                (
                    skill_correct
                    /
                    skill_total
                ) * 100
            )

        else:

            skill_percentage = 0


        # Determine skill proficiency
        if skill_percentage < 40:

            skill_level = "Beginner"

        elif skill_percentage < 60:

            skill_level = "Basic"

        elif skill_percentage < 80:

            skill_level = "Intermediate"

        else:

            skill_level = "Advanced"


        cursor.execute(
            """
            INSERT INTO learner_skill_performance
            (
                user_id,
                skill,
                correct_answers,
                total_answers,
                proficiency_score,
                proficiency_level
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                session["user_id"],
                skill,
                skill_correct,
                skill_total,
                skill_percentage,
                skill_level
            )
        )

    # -----------------------------------------------------
    # XP
    # -----------------------------------------------------

    xp_earned = score * 10


    cursor.execute(
        """
        UPDATE users

        SET xp = xp + ?

        WHERE id = ?
        """,
        (
            xp_earned,
            session["user_id"]
        )
    )


    # -----------------------------------------------------
    # Level
    # -----------------------------------------------------

    if proficiency_level == "Beginner":

        new_level = 1

    elif proficiency_level == "Intermediate":

        new_level = 2

    else:

        new_level = 3


    cursor.execute(
        """
        UPDATE users

        SET level =
            CASE
                WHEN level > ? THEN level
                ELSE ?
            END

        WHERE id = ?
        """,
        (
            new_level,
            new_level,
            session["user_id"]
        )

    )
    connection.commit()
    connection.close()
    assessment_guidance = get_initial_assessment_guidance(
    session["user_id"]
)

    
    return render_template(
    "assessment_result.html",

    score=score,

    total_questions=
        total_questions,

    percentage=
        round(percentage),

    proficiency_level=
        proficiency_level,

    xp_earned=
        xp_earned,

    assessment_guidance=
        assessment_guidance
)







@app.route("/change-language", methods=["POST"])
def change_language():

    if "user_id" not in session:
        return redirect("/login")

    preferred_language = request.form.get(
        "preferred_language",
        "English"
    ).strip()

    learning_language = request.form.get(
        "learning_language",
        "English"
    ).strip()


    # Languages currently supported
    allowed_languages = [
        "English",
        "Telugu",
        "Hindi"
    ]


    # Check preferred language

    if preferred_language not in allowed_languages:
        preferred_language = "English"


    # Check learning language

    if learning_language not in allowed_languages:
        learning_language = "English"


    # Update database

    connection = get_db_connection()

    connection.execute(
        """
        UPDATE users

        SET preferred_language = ?,
            learning_language = ?

        WHERE id = ?
        """,
        (
            preferred_language,
            learning_language,
            session["user_id"]
        )
    )

    connection.commit()

    connection.close()


    # Update session

    session["preferred_language"] = preferred_language

    session["learning_language"] = learning_language

        # -----------------------------------------------------
        # -----------------------------------------------------
    # CHECK INITIAL ASSESSMENT
    # -----------------------------------------------------
    assessment_connection = get_db_connection()

    assessment_done = assessment_connection.execute(
        """
        SELECT COUNT(*)
        FROM assessment_attempts
        WHERE user_id = ?
        """,
        (session["user_id"],)
    ).fetchone()[0]

    assessment_connection.close()

    # New user / assessment not completed
    if assessment_done == 0:
        return redirect("/assessment")

    # Assessment already completed
    return redirect("/dashboard")
# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# =========================================================
# ERROR HANDLER
# =========================================================

@app.errorhandler(404)
def page_not_found(error):

    return """
    <h1>404 - Page Not Found</h1>

    <p>
        The page you are looking for does not exist.
    </p>

    <a href="/">
        Go Home
    </a>
    """, 404


# =========================================================
# START APPLICATION
# =========================================================

if __name__ == "__main__":

    create_database()

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )