const fs = require('fs');
const path = require('path');
const Sequelize = require('sequelize');
const basename = path.basename(module.filename);
const sequelize = new Sequelize('test', 'root', 'root', { // db name, username, password
    host: '127.0.0.1',
    dialect: 'mysql',
    logging: false,
    timezone: '+00:00',
    operatorsAliases: false,
    define: {
        underscored: true,
        timestamps: false
    }
});

let db = {
    sequelize,
    Sequelize,
};

$or = db.sequelize.Op.or;
$and = db.sequelize.Op.and;

db.authors = sequelize
    .define('authors', {
        author_id: {
            type: Sequelize.DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: Sequelize.DataTypes.STRING,
        created_at: Sequelize.DataTypes.DATE
    },
    {
        freezeTableName: true
    }
);

db.books = sequelize
    .define('books', {
        book_id: {
            type: Sequelize.DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        author_id: Sequelize.DataTypes.INTEGER,
        name: Sequelize.DataTypes.STRING,
        created_at: Sequelize.DataTypes.DATE
    },
    {
        freezeTableName: true
    }
);

Object.keys(db).forEach(model_name => {
    db[model_name].find_one = db[model_name].findOne;
    db[model_name].find_all = db[model_name].findAll;
    db[model_name].find_or_create = db[model_name].findOrCreate;
    db[model_name].find_and_count_all = db[model_name].findAndCountAll;
    db[model_name].belongs_to = db[model_name].belongsTo;
    db[model_name].has_one = db[model_name].hasOne;
    db[model_name].has_many = db[model_name].hasMany;
    db[model_name].belongs_to_many = db[model_name].belongsToMany;
});

db.authors.has_many(db.books, { as: 'books', foreignKey: 'author_id' });

db.books.belongs_to(db.authors, { as: 'author', foreignKey: 'author_id' });

module.exports = db;
