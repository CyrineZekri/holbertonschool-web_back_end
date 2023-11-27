export default class Currency{
  constructor(code,name){
    if(typeof code !== 'string') throw TypeError('Code must be a string');
    if(typeof name !== 'string') throw TypeError('Code must be a string');
    this._code = code;
    this._name = name
  }
  get name(){
    return this._name;
  }
  get code(){
    return this._code;
  }
  set name(value){
    if(typeof value !== 'string') throw TypeError('Code must be a string');
    this._name=value;
  }    set code(value){
    if(typeof value !== 'string') throw TypeError('Code must be a string');
    this._code = value;
  }
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }

}
