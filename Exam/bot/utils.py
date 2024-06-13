from aiogram.utils.i18n import gettext as _

from db.models import Book


def caption_book(book: Book):
    caption = """
{title}: {book_name}
{author}: {book_author}
{janr}: {book_genre} 
{page}: {book_page}
{vol}: {book_vol}
{description}: {book_description}
{price}: {book_price}
    """.format(title = _("🔹 Title") ,
               book_name = book.title,
               author = _("✍🏻Author"),
               book_author = book.author,
               janr=_("🟤 Genre"),
               book_genre=book.category.name,
               page=_("📑 Page"),
               book_page=book.page,
               vol=_("📕 Vol"),
               book_vol=book.vol.value,
               description=_("📖 Description"),
               book_description=book.description,
               price=_("💸 Price"),
               book_price=book.price,
               )
    return caption
