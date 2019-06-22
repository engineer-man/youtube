const express = require('express');
const moment = require('moment');
const parser = require('body-parser');
const db = require('./models');
const app = express();

app.use(parser.json());

app.use(async (req, res, next) => {
    if (req.headers.authorization !== '123abc') {
        return res
            .status(401)
            .send();
    }

    next();
});

// authors resource
app.get('/api/v1/authors', async (req, res) => {
    let authors = await db.authors
        .find_all();

    return res
        .status(200)
        .send(authors);
});

app.get('/api/v1/authors/:author_id', async (req, res) => {
    const author_id = req.params.author_id;

    let author = await db.authors
        .find_one({
            where: {
                author_id
            }
        });

    if (!author) {
        return res
            .status(404)
            .send();
    }

    return res
        .status(200)
        .send(author);
});

app.post('/api/v1/authors', async (req, res) => {
    const { name } = req.body;

    let author = await db.authors
        .create({
            name,
            created_at: moment().format()
        });

    //return res
    //    .status(201)
    //    .send(author);
    return res
        .status(204)
        .send();
});

app.put('/api/v1/authors/:author_id', async (req, res) => {
    const author_id = req.params.author_id;
    const { name } = req.body;

    let author = await db.authors
        .find_one({
            where: {
                author_id
            }
        });

    if (!author) {
        return res
            .status(404)
            .send();
    }

    author.name = name;

    await author.save();

    return res
        .status(200)
        .send(author);
    //return res
    //    .status(204)
    //    .send();
});

app.delete('/api/v1/authors/:author_id', async (req, res) => {
    const author_id = req.params.author_id;

    let author = await db.authors
        .find_one({
            where: {
                author_id
            }
        });

    if (!author) {
        return res
            .status(404)
            .send();
    }

    await author.destroy();

    return res
        .status(204)
        .send();
});

// authors -> books endpoints
app.get('/api/v1/authors/:author_id/books', async (req, res) => {
    const author_id = req.params.author_id;

    let author = await db.authors
        .find_one({
            where: {
                author_id
            },
            include: [
                {
                    model: db.books,
                    as: 'books'
                }
            ]
        });

    if (!author) {
        return res
            .status(404)
            .send();
    }

    return res
        .status(200)
        .send(author.books);
});

app.post('/api/v1/authors/:author_id/books', async (req, res) => {
    const author_id = +req.params.author_id;
    const { name } = req.body;

    let author = await db.authors
        .find_one({
            where: {
                author_id
            }
        });

    if (!author) {
        return res
            .status(404)
            .send();
    }

    let book = await db.books
        .create({
            author_id,
            name,
            created_at: moment().format()
        });

    return res
        .status(201)
        .send(book);
    //return res
    //    .status(204)
    //    .send();
});

// books endpoints
app.get('/api/v1/books', async (req, res) => {
    let books = await db.books
        .find_all();

    return res
        .status(200)
        .send(books);
});

app.get('/api/v1/books/:book_id', async (req, res) => {
    const book_id = req.params.book_id;

    let book = await db.books
        .find_one({
            where: {
                book_id
            }
        });

    if (!book) {
        return res
            .status(404)
            .send();
    }

    return res
        .status(200)
        .send(book);
});

app.put('/api/v1/books/:book_id', async (req, res) => {
    const book_id = req.params.book_id;
    const { name } = req.body;

    let book = await db.books
        .find_one({
            where: {
                book_id
            }
        });

    if (!book) {
        return res
            .status(404)
            .send();
    }

    book.name = name;

    await book.save();

    return res
        .status(200)
        .send(book);
    //return res
    //    .status(204)
    //    .send();
});

app.delete('/api/v1/books/:book_id', async (req, res) => {
    const book_id = req.params.book_id;

    let book = await db.books
        .find_one({
            where: {
                book_id
            }
        });

    if (!book) {
        return res
            .status(404)
            .send();
    }

    await book.destroy();

    return res
        .status(204)
        .send();
});

// author -> book combo endpoints
app.get('/api/v1/author-books', async (req, res) => {
    let authors = await db.authors
        .find_all({
            include: [
                {
                    model: db.books,
                    as: 'books'
                }
            ]
        });

    return res
        .status(200)
        .send(authors);
});

app.get('/api/v1/author-books/:author_id', async (req, res) => {
    const author_id = req.params.author_id;

    let author = await db.authors
        .find_one({
            where: {
                author_id
            },
            include: [
                {
                    model: db.books,
                    as: 'books'
                }
            ]
        });

    if (!author) {
        return res
            .status(404)
            .send();
    }

    return res
        .status(200)
        .send(author);
});

app.listen(9000);
