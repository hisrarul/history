const products = [];

const path = require('path')
const fs = require('fs')

module.exports = class Product {
    constructor(titl) {
        this.title = titl;
    }
    save() {
        const p = path.join(
          path.dirname(process.mainModule.filename),
          'data',
          'products.json'
        );
        fs.readFile(p, (err, fileContent) => {
          let products = [];
          if (!err) {
            products = JSON.parse(fileContent);
          }
          products.push(this);
          fs.writeFile(p, JSON.stringify(products), err => {
            console.log(err);
          });
        });
      }
    // save() {
    //     // products.push(this);
    //     const p = path.join(
    //         path.dirname(process.mainModule.filename),
    //         'data',
    //         'products.json'
    //     );
    //     console.log(p)
    //     fs.readFile(p, (err, fileContent) => {
    //         if (!err) {
            
    //             products = JSON.parse(fileContent);
    //         }
    //         products.push(this)
    //         fs.writeFile(p, JSON.stringify(products), (err) => {
    //             console.log(err);
    //         });
    //     });
    // }

    static fetchAll(cb) {
        const p = path.join(
          path.dirname(process.mainModule.filename),
          'data',
          'products.json'
        );
        fs.readFile(p, (err, fileContent) => {
          if (err) {
            cb([]);
          }
          cb(JSON.parse(fileContent));
        });
      }

    // static fetchAll(cb) {
    //     const p = path.join(
    //         path.dirname(process.mainModule.filename),
    //         'data',
    //         'products.json'
    //     );
    //     fs.readFile(p, (err, fileContent) => {
    //         if (err) {
    //             cb([]);
    //         }
    //         cb(JSON.parse(fileContent));
    //     });
    // }
};