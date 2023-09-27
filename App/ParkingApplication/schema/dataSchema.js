const mongoose = require('mongoose');

const dataSchema = new mongoose.Schema({
    accounts: [accountsSchema],
    liveData: [string]
});

const accountsSchema = new mongoose.Schema({
    studentId: string,
    registered: [{plate: string, tagId: string}]
})
const User = mongoose.model('account', dataSchema);
module.exports = User;