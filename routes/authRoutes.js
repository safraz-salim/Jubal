const express = require('express');
const router = express.Router();
const auth = require('../middleware/authMiddleware');
const { register, login, getUser } = require('../controllers/authController');

router.post('/register', register);
router.post('/login', login);
router.get('/me', auth, getUser);

module.exports = router;