<template>
    <a-card>
        <a-spin class="center" v-if="loading" />
        <a-table v-cloak :data-source="ordersData" :columns="columns" rowKey="id">
            <span slot="created_at" slot-scope="created_at">
                {{new Date(created_at).toLocaleDateString()}}  
            </span>
            <span slot="price" slot-scope="price">
                {{price}} Fcfa
            </span>
            <span slot-scope="status" slot="status">
                <a-tag v-if="status=='cancel'" color="red">annulée</a-tag>
                <a-tag v-if="status=='search'" color="blue">en attente...</a-tag>
                <a-tag v-if="status=='end'" color="blue">terminée</a-tag>
            </span>
            <span slot="action" slot-scope="action">
                <router-link :to="'/order/'+action.id" >Details</router-link>
            </span>
        </a-table>
    </a-card>
</template>

<script>
import Axios  from 'axios'


const columns = [
    {
        title:"Date",
        key:"created_at",
        dataIndex:'created_at',
        scopedSlots:{customRender:"created_at"}
    },
    {
        title:"Coût",
        key:"price",
        dataIndex:'price',
        scopedSlots:{customRender:"price"}
    },
    {
        title:"Statut",
        key:"status",
        dataIndex:'status',
        scopedSlots:{customRender:"status"}
    },
    {
        title:"ACTION",
        key:"action",
        scopedSlots:{customRender:"action"}
    }
]

export default {
    // props:{
    //     ordersData:[]
    // },
    data(){
        var ordersData = []
        return {
            ordersData,
            columns,
            showOrderDetail:false,
            loading:true,
        }
    },
    mounted:function(){
        console.log(this.ordersData);
    },
    beforeMount:function(){
         Axios.get('http://127.0.0.1:8000/orders/').then((response)=>{
            this.ordersData = response.data
            this.loading = false
         })

        console.log(this.ordersData);
    },
}
</script>