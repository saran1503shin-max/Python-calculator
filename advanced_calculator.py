
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import math

BOT_TOKEN = "YOUR_BOT_TOKEN"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Calculator Bot!\n"
        "Use:\n"
        "/add 5 2\n"
        "/sub 5 2\n"
        "/mul 5 2\n"
        "/div 5 2\n"
        "/sqrt 25"
    )

# Addition
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    a = float(context.args[0])
    b = float(context.args[1])
    await update.message.reply_text(f"Result: {a + b}")

# Subtraction
async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    a = float(context.args[0])
    b = float(context.args[1])
    await update.message.reply_text(f"Result: {a - b}")

# Multiplication
async def mul(update: Update, context: ContextTypes.DEFAULT_TYPE):
    a = float(context.args[0])
    b = float(context.args[1])
    await update.message.reply_text(f"Result: {a * b}")

# Division
async def div(update: Update, context: ContextTypes.DEFAULT_TYPE):
    a = float(context.args[0])
    b = float(context.args[1])

    if b == 0:
        await update.message.reply_text("Cannot divide by zero")
    else:
        await update.message.reply_text(f"Result: {a / b}")

# Square Root
async def sqrt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    a = float(context.args[0])
    await update.message.reply_text(f"Result: {math.sqrt(a)}")

# Main
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("sub", sub))
app.add_handler(CommandHandler("mul", mul))
app.add_handler(CommandHandler("div", div))
app.add_handler(CommandHandler("sqrt", sqrt))

print("Bot Running...")
app.run_polling()
