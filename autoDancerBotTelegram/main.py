from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import update

the_song = ["הנה הוא שומע את המנגינה",
            "מתחבר כמו אוטומט לזרם",
            "בגופו רוקע על האדמה",
            "הוא נמצא עכשיו בתוך הקצב",
            "לחן סטריאופוני אור כחול אדום",
            "תנו לו לדבר עם הרגליים",
            "כל המיקרופונים כאן על הבמה",
            "זהו הרקדן האוטומטי",
            "את המנגינה הוא חי",
            "גופו מחושמל",
            "בתוכו הלב פועם",
            "בקצב קצב",
            "עוד ריקוד אחד ודי",
            "נפסק החשמל",
            "הרקדן נשאר דומם",
            "כמו אבן אבן",
            "אההההההההה אה אה",
            "רגל מרחפת צחוק על הפנים",
            "שריר בשריר נוגע לא נוגע",
            "מי שם מייללת כמו החתולים",
            "איך הוא לא מפסיק להתנועע",
            "תן לו את הקצב, תן את הצלילים",
            "יש לו זרם יש לו נשימה",
            "ווה ווה בגיטרות",
            "פאזים על הבס",
            "בין צלילי הרוק והנשמה",
            "את המנגינה הוא חי...",
            "רעש באוזניים תן לו את הביט",
            "עלה איתו לטון יותר גבוה",
            "קופסאות של קצב כל גופו מרעיד",
            "תן לו את המוזיקה לשמוע",
            "תן לו את הקצב, תן את הנשמה",
            "כל גופו רועד מצחוק מזיע",
            "על רצפה מפלסטיק כך הוא מתפרק",
            "זהו הרקדן האוטומטי",
            "את המנגינה הוא חי.."]

def start(update: update, context: CallbackContext) -> None:
    update.message.reply_text("היושששש בואו נשיר")

def reply(update: update, context: CallbackContext) -> None:
    message = "זאת לא שורה בשירררר"
    try:
        index = [i for i, s in enumerate(the_song) if s.startswith(update.message.text)][0]
        if the_song[index] != update.message.text:
            message = the_song[index][len(update.message.text):]
        elif index + 1 == len(the_song):
            message = "נגמר השיררר"
        else:
            message = the_song[index + 1]
        update.message.reply_text(message)
    except:
        update.message.reply_text(message)

def main() -> None:
    updater = Updater("1428797059:AAH8V4Umm8u6lkzGYFdLp7IgpCTdGpcZB1g", use_context=True)
    dispacher = updater.dispatcher
    dispacher.add_handler(CommandHandler("start", start))

    dispacher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
