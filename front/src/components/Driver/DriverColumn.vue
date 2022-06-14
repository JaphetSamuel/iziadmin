<template>
    <main>
    <a-page-header title="Details">
        <template #sub-title>
            <a-tag class="tag-status" :class="driver.is_enabled ? 'ant-tag-primary' : 'ant-tag-muted'">
                {{ driver.is_enabled ? "ACTIVE" : "DESACTIVE" }}
            </a-tag>
        </template>
    </a-page-header>
    <a-card style="heigth=100%">
        <a-card-meta>
            <template #title>
                <a-row>
                    <a-col :span="12">
                        <h5>Details</h5>
                    </a-col>
                    <a-col :span="12" type="flex" align="end">
                        <a-switch checked-children="actif" un-checked-children="inactif" v-bind:checked="record.is_enabled" @change="switchStatus" />
                    </a-col>
                </a-row>    
            </template>
            
               
        </a-card-meta>
        <a-row>
                <a-col span="6">
                    <a-avatar :size="80" shape="square" v-if="record.get_picture" :src="record.get_picture" alt="photo de profile"/>
                    <a-avatar  v-else shape="square" icon="user" :size="64" />
                    <a-tag style="margin-left:7px;" :color="record.is_online? 'green':'red'">
                        {{record.is_online ? "En ligne" : "Hors ligne"}}
                    </a-tag>
                </a-col>
                <a-col span="18">
                    <h3>{{record.firstname}} {{record.lastname}}</h3>
                </a-col>
        </a-row>
        <a-tabs>
            <a-tab-pane key="info" tab="infos">
                <a-space size="large" align="end">
                    <a-button icon="download">
                    <a :href="record.get_licence">permis de conduit</a>
                    </a-button>
                    <a-tag size="large" :color="record.order_id? 'orange':'blue'">
                        {{record.order_id? "occupé": "libre"}}
                    </a-tag>
                </a-space>
                <a-descriptions style="margin-top:25px;">
                     <a-description-item >
                            <template #label>
                                <b>Email   </b>
                            </template>
                            <span>
                                {{record.email}}
                            </span>
                        </a-description-item>
                        <a-description-item >
                            <template #label>
                                <b>Contact   </b>
                            </template>
                            <span>
                                {{record.phone}}
                            </span>
                        </a-description-item>
                        <a-description-item >
                            <template #label>
                                <b>inscrit le   </b>
                            </template>
                            <span>
                                {{new Date(record.created_at).toLocaleDateString("fr-FR")}}
                            </span>
                        </a-description-item>
                        <a-description-item >
                            <template #label>
                                <b>note generale   </b>
                            </template>
                            <h4>
                                {{record.note}}
                            </h4>
                        </a-description-item>
                </a-descriptions>
                <a-descriptions title="Véhicule">
                    <a-description-item>
                        <template #label>
                            <b>Marque   </b>
                        </template>
                        <span>
                            {{record.car_brand}}
                        </span>
                    </a-description-item>
                    <a-descriptions-item>
                        <template #label>
                            <b>Modèle   </b>
                        </template>
                        <span>
                            {{record.car_model}}
                        </span>
                    </a-descriptions-item>
                    <a-description-item>
                        <template #label>
                            <b>Immatriculation  </b>
                        </template>
                        <span>
                            {{record.immatriculation}}
                        </span>
                    </a-description-item>
                </a-descriptions>
            </a-tab-pane>
            <a-tab-pane key="order" tab="course">
                <a-table :data-source="order_list" :columns="orders_columns" row-key="id" size="small">

                    <span slot="date" slot-scope="date">
                        {{new Date(date).toLocaleDateString("fr-FR")}}
                    </span>

                    <span slot="trajet" slot-scope="trajet">
                        <a-timeline>
                            <a-timeline-item> {{trajet.from_name}}</a-timeline-item>
                            <a-timeline-item color="red" icon="map"> {{trajet.to_name}}</a-timeline-item>
                        </a-timeline>
                    </span>
                    <span slot="price" slot-scope="price">
                        {{price}} Fcfa
                    </span>
                    <span slot="action" slot-scope="action">
                        <router-link :to="'/order/'+action.id">
                            Voir
                        </router-link>
                    </span>
                </a-table>
            </a-tab-pane>
            <a-tab-pane key="subscription" tab="transactions">
                <a-spin v-if="transLoading"/>
                <a-collapse v-else>
                    <a-collapse-panel v-for="transaction in transactions" :key="transaction.id">
                        <template #header>
                            {{transaction.bundle.name}}
                            <a-tag :color="transaction.is_actif? 'green':'grey'">
                                {{transaction.is_actif? "actif": "inactif"}}
                            </a-tag>
                        </template>
                        <a-row>
                            <a-col :span="6">
                                <a-statistic :title="transaction.bundle.name" :value="transaction.bundle.amount" suffix="Fcfa" />
                            </a-col>
                            <a-col :span="18">
                                <a-descriptions :column="2">
                                    <a-descriptions-item label="reference">
                                        {{transaction.reference}}
                                    </a-descriptions-item>
                                    <a-descriptions-item label="achat effectué le">
                                        {{new Date(transaction.created_at).toLocaleDateString("fr-FR")}}
                                    </a-descriptions-item>
                                    <a-descriptions-item label="Debut">
                                        {{new Date(transaction.start_at).toLocaleDateString("fr-FR")}}
                                    </a-descriptions-item>
                                    <a-descriptions-item :label="transaction.is_actif ? 'prend fin le':'a pris fin le'">
                                        {{new Date(transaction.end_at).toLocaleDateString("fr-FR")}}
                                    </a-descriptions-item>
                                </a-descriptions>
                            </a-col>
                        </a-row>
                    </a-collapse-panel>
                </a-collapse>
            </a-tab-pane>
            <a-tab-pane key="statistique" tab="stats">
                <a-row>
                    <a-col :span="6">
                        <a-statistic title="nombre de voyage" :value="order_list.length"/>
                    </a-col>
                    <a-col :span="6">
                        <a-statistic title="Commande(s) annulée(s)" :value="canceled_orders.length" :suffix="'/'+orders_count" />
                    </a-col>
                    <a-col :span="6">
                        <a-statistic title="Commande(s) terminée(s)" :value="ended_orders.length" :suffix="'/'+orders_count"/>
                    </a-col>
                </a-row>
            </a-tab-pane>
        </a-tabs>
    </a-card>
    </main>
</template>

<script>
import Axios from 'axios'
import WidgetCounterVue from '../Widgets/WidgetCounter.vue'

const orders_columns = [
    {
        key:"date",
        title:"Date et heure",
        dataIndex:"driver_start_at",
        scopedSlots:{customRender:"date"}
    },
    {
        key:"Trajet",
        title:"Trajet",
        scopedSlots:{customRender:"trajet"}
    },
    {
        key:"price",
        title:"Coût",
        dataIndex:"price",
        scopedSlots:{customRender:"price"}
    },
    {
        key:"status",
        title:"Statut",
        dataIndex:"status",
        scopedSlots:{customRender:"status"}
    },
    {
        key:"action",
        title:"Action",
        scopedSlots:{customRender:"action"}
    }
]


export default{
    components:{
        WidgetCounterVue
    },
    data(){
        return {
            record:{},
            order_list: [],
            orders_columns,
            transactions:[],
            transLoading:true,
        } 
    },
    methods:{
        switchStatus(){
            Axios.post("http://127.0.0.1:8000/driver/enable", {
                driver_id:this.record.id,
                enable:this.record.is_enabled?"no":"yes"
            }).then(response => {
                this.$message.success("Status modifié avec succès");
                this.record.is_enabled = response.data;
                console.log(this.record);
            }).catch(error => {
                this.$message.error("Erreur lors de la modification du status");
            });
        },
    },
    computed:{
        orders_count:function(){
            return this.order_list.length;
        },
        canceled_orders:function(){
            return this.order_list.filter(order => order.status == "cancel");
        },
        ended_orders:function(){
            return this.order_list.filter(order => order.status == "end");
        },
    },
    mounted:function(){
        console.log(this.$route.params.id);
        Axios.get("http://127.0.0.1:8000/driver/"+this.$route.params.id).then(response => {
            this.record = response.data;
            console.log(this.record);
        })

        Axios.get("http://localhost:8000/orders/driver_commande/"+this.$route.params.id).then(response => {
            this.order_list = response.data
            console.log(this.order_list);
        })

        Axios.get('http://localhost:8000/driver/getsubscriptionfor/'+this.$route.params.id).then(response => {
            this.transactions = response.data;
            console.log(this.transactions);
            this.transLoading = false 
        })
    }
}

</script>