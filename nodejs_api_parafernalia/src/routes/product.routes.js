const router = require('express-promise-router')();
const productController = require('../controllers/product.controller');

router.get('/discounts/:idP/:idU', productController.findProductById);


module.exports = router;