import view
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'Привет {update.effective_user.first_name}! вот мой список команд:'
        f'\n/add - добавить данные имя/фамилия/тел/д.р/раб записей через пробел \n'
        f'/show - показать таблицы \n')


app = ApplicationBuilder().token("token").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("show", view.output_book))
app.add_handler(CommandHandler("add", view.add_data))
app.run_polling()

