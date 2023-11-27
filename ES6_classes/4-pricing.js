export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') throw TypeError('Amount must be a number');
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== 'number') throw TypeError('Amount must be a number');
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = value;
  }

  displayFullPrice() {
    const currencyAll = this._currency.displayFullCurrency();
    return `${this._amount} ${currencyAll}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
