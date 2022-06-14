import Axios from 'axios'


export const getAllOrders = function (){
    return Axios.get('http://127.0.0.1:8000/orders/')
}

/**
 * 
 * 
 * Menu : 
 * 1 - Dashboard
 * 2 - Commande
 */
