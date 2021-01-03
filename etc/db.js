use ddd;

db.createCollection("user");
db.user.createIndex({"user_id": 1}, {"unique": true})
db.user.createIndex({"id": 1}, {"unique": true})

db.createCollection("video");
db.video.createIndex({"video_id": 1}, {"unique": true})
db.video.createIndex({"id": 1}, {"unique": true})