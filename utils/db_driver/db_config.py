mongo_database = 'dev-nlp'
mongo_url = 'mongodb://resource-admin:Lexica_Powerof10@lexica-uat-shard-00-00-8baaz.mongodb.net:27017,lexica-uat-shard-00-01-8baaz.mongodb.net:27017,lexica-uat-shard-00-02-8baaz.mongodb.net:27017/'+mongo_database+'?ssl=true&replicaSet=lexica-uat-shard-0&authSource=admin'

ext_nlp_database = 'ext-nlp'
ext_nlp_url = 'mongodb://resource-admin:Lexica_Powerof10@lexica-uat-shard-00-00-8baaz.mongodb.net:27017,lexica-uat-shard-00-01-8baaz.mongodb.net:27017,lexica-uat-shard-00-02-8baaz.mongodb.net:27017/'+ext_nlp_database+'?ssl=true&replicaSet=lexica-uat-shard-0&authSource=admin'

mongo_chatbot_database = 'chatbot'
mongo_chatbot_url = 'mongodb://resource-admin:Lexica_Powerof10@lexica-uat-shard-00-00-8baaz.mongodb.net:27017,lexica-uat-shard-00-01-8baaz.mongodb.net:27017,lexica-uat-shard-00-02-8baaz.mongodb.net:27017/'+mongo_chatbot_database+'?ssl=true&replicaSet=lexica-uat-shard-0&authSource=admin'

hku_nlp_database = 'hku-nlp'
hku_nlp_url = 'mongodb://resource-admin:Lexica_Powerof10@lexica-shard-00-00-tusrw.mongodb.net:27017,lexica-shard-00-01-tusrw.mongodb.net:27017,lexica-shard-00-02-tusrw.mongodb.net:27017/'+hku_nlp_database+'?ssl=true&replicaSet=lexica-shard-0&authSource=admin'

hku_chatbot_database = 'chatbot'
hku_chatbot_url = 'mongodb://resource-admin:Lexica_Powerof10@lexica-shard-00-00-tusrw.mongodb.net:27017,lexica-shard-00-01-tusrw.mongodb.net:27017,lexica-shard-00-02-tusrw.mongodb.net:27017/'+hku_chatbot_database+'?ssl=true&replicaSet=lexica-shard-0&authSource=admin'
dev_chatbot = 'dev-chatbot'
dev_nlp = 'dev-nlp'
ext_chatbot = 'chatbot'
ext_nlp = 'ext-nlp'
hku_chatbot = 'chatbot'
hku_nlp = 'hku-nlp'
mongo_config = {
    'dev': {
        'chatbot': {
            'url': 'mongodb://resource-admin:Lexica_Powerof10@lexica-uat-shard-00-00-8baaz.mongodb.net:27017,lexica-uat-shard-00-01-8baaz.mongodb.net:27017,lexica-uat-shard-00-02-8baaz.mongodb.net:27017/'+dev_chatbot+'?ssl=true&replicaSet=lexica-uat-shard-0&authSource=admin',
            'database': dev_chatbot
        },
        'nlp': {
            'url': 'mongodb://resource-admin:Lexica_Powerof10@lexica-uat-shard-00-00-8baaz.mongodb.net:27017,lexica-uat-shard-00-01-8baaz.mongodb.net:27017,lexica-uat-shard-00-02-8baaz.mongodb.net:27017/'+dev_nlp+'?ssl=true&replicaSet=lexica-uat-shard-0&authSource=admin',
            'database': dev_nlp
        }
    },
    'ext': {
        'chatbot': {
            'url': 'mongodb://resource-admin:Lexica_Powerof10@lexica-uat-shard-00-00-8baaz.mongodb.net:27017,lexica-uat-shard-00-01-8baaz.mongodb.net:27017,lexica-uat-shard-00-02-8baaz.mongodb.net:27017/'+ext_chatbot+'?ssl=true&replicaSet=lexica-uat-shard-0&authSource=admin',
            'database': ext_chatbot
        },
        'nlp': {
            'url': 'mongodb://resource-admin:Lexica_Powerof10@lexica-uat-shard-00-00-8baaz.mongodb.net:27017,lexica-uat-shard-00-01-8baaz.mongodb.net:27017,lexica-uat-shard-00-02-8baaz.mongodb.net:27017/'+ext_nlp+'?ssl=true&replicaSet=lexica-uat-shard-0&authSource=admin',
            'database': ext_nlp
        }
    },
    'hku': {
        'chatbot': {
            'url': 'mongodb://resource-admin:Lexica_Powerof10@lexica-shard-00-00-tusrw.mongodb.net:27017,lexica-shard-00-01-tusrw.mongodb.net:27017,lexica-shard-00-02-tusrw.mongodb.net:27017/'+hku_chatbot+'?ssl=true&replicaSet=lexica-shard-0&authSource=admin',
            'database': hku_chatbot
        },
        'nlp': {
            'url': 'mongodb://resource-admin:Lexica_Powerof10@lexica-shard-00-00-tusrw.mongodb.net:27017,lexica-shard-00-01-tusrw.mongodb.net:27017,lexica-shard-00-02-tusrw.mongodb.net:27017/'+hku_nlp+'?ssl=true&replicaSet=lexica-shard-0&authSource=admin',
            'database': hku_nlp
        }
    }
}
