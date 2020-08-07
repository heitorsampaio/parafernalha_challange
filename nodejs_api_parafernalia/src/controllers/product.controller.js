const db = require('../config/database');

exports.findProductById = async (req, res) => {
  const idP = parseInt(req.params.idP);
  const idU = parseInt(req.params.idU);

  const responseU = await db.query(
    'SELECT * FROM users WHERE id = $1',
    [idU],
  );
  const responseP = await db.query(
    'SELECT * FROM products WHERE id = $1',
    [idP],
  );
  
  const productPrice = responseP.rows[0].price;
  const baseDiscount = responseP.rows[0].base_discount_percent;
  const birthday = responseU.rows[0].birthdate;
  const now = new Date;
  const blackFriday = new Date(0, 10, 25);
  let totalDiscount = baseDiscount;
  

  const birthdayCond = (birthday.getDate() === now.getDate()) && (birthday.getMonth() === now.getMonth());
  const blackfridayCond = (blackFriday.getDate() === now.getDate()) && (blackFriday.getMonth() === now.getMonth());
  

  if (birthdayCond) { totalDiscount += 5.0 };
  if (blackfridayCond) { totalDiscount += 10.0 };
  if (totalDiscount > 25.0) { totalDiscount= 25.0 }
  

  const precoDescontado = productPrice*(100 - totalDiscount)/100

  const response = { "total_discount": totalDiscount,
                    "final_price": precoDescontado}

  res.status(200).send(response);
};
