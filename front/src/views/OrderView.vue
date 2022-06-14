<template>
    <a-row>
        <span>Order</span>
        <order-table :ordersData="orders" />
    </a-row>
</template>
<script>
import useOrderStore from "../store/orderStore"
import OrderTableVue from "../components/Order/OrderTable.vue"
import {getAllOrders} from "../services/orderService"
import OrderTable from '../components/Order/OrderTable.vue'



export default {
  components: { OrderTable },
    data(){
        return {
            orders:[]
        }
    },
}
</script>