import { Calc } from './lib/calc';

class Main {

    constructor() {
        try {
            document.getElementById('body').innerHTML = Calc.add(5, 6).toString();
        } catch(e) {
            console.log(Calc.add(5, 6));
        }

    }

}

new Main();
