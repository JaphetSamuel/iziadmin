<template>
    <a-row  style="background-color:white; padding:20px" >
        <a-col :span="24">
            <a-page-header @back="goBack">
                <template #title>
                    Commande #{{order.id}}
                </template>
                <template slot="tag">
                    <a-tag>{{order.status}}</a-tag>
                </template>
                <template #extra>
                            <a-statistic title="coût" :value="order.price" sufix="Fcfa"/>
                </template>
            </a-page-header>
        </a-col>
        <a-col :span="24">
            <a-descriptions>
                <a-descriptions-item label="heure de la commande">
                    {{order.created_at}}
                </a-descriptions-item>
                <a-descriptions-item label="service">
                    {{order.types}}
                </a-descriptions-item>
                <a-descriptions-item label="distance">
                    {{order.distance}} m
                </a-descriptions-item>
                <a-descriptions-item label="durée">
                    {{order.duration}} min
                </a-descriptions-item>
                <a-descriptions-item label="emplacement">
                    {{order.from_name}} -- {{order.to_name}}
                </a-descriptions-item>
            </a-descriptions>
        </a-col>
        <a-col :span="24">
            
                 
                    <a-descriptions title="info client" bordered>
                        <a-descriptions-item label="Nom et Prenom">
                            {{client.firstname}} {{client.lastname}}
                        </a-descriptions-item>
                        <a-descriptions-item label="contact">
                            {{client.phone}}
                        </a-descriptions-item>
                        <a-descriptions-item label="inscrit le ">
                            {{client.created_at}}
                        </a-descriptions-item>
                    </a-descriptions>
                    <one-map-widget-vue :color="order.status == 'end'? 'red':'blue'" :polygone="order.path" height="80vh"/>
                
        </a-col>
    </a-row>
</template>
<script>
import Axios from "axios"
import OneMapWidgetVue from "../components/Map/OneMapWidget.vue"

// details order
export default {
    components:{
        OneMapWidgetVue
    },
    props:{
        id:Number,
    },
    data(){
        return {
            order:{},
            client:{}
        }
    },
    methods: {
        goBack(){
            this.$router.go(-1)
        },
    },
    mounted:function(){
        Axios.get('http://127.0.0.1:8000/orders/'+this.$route.params.id).then((response)=>{
            this.order = response.data
            console.log(this.order);
            Axios.get('http://127.0.0.1:8000/customers/'+this.order.customer_id).then((response)=>{
                this.client = response.data
                console.log(this.client);
            })
        })
    }
}
</script>