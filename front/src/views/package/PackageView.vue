<template>
    <main style="background-color:white">
        <a-row>
            <a-col :span="24">
                <a-page-header title="Liste des packs pour conducteur">
                    <template #extra>
                        <router-link to="/package/new">
                        <a-button>
                            <a-icon type="plus" />
                                Ajouter
                        </a-button>
                        </router-link>
                    </template>
                </a-page-header>
            </a-col>
            <a-col :span="24">
                <a-table :data-source="packs" :columns="pack_columns" rowKey="id">
                    <span slot="duration" slot-scope="duration">
                        <span class="bold" style="font-size:60px">{{duration}}</span> <span>Jours</span>
                    </span>
                    <span slot="amount" slot-scope="amount">
                        <span class="bold" style="font-size:30px">{{amount}}</span> Fcfa
                    </span>
                    <span slot="action" slot-scope="action">
                        <a-button @click="showDetailModal(action)"> voir </a-button>
                    </span>
                </a-table>
            </a-col>
        </a-row>
        <a-modal :visible="viewMode"
        @cancel="modalCancel"
        @ok="modalCancel"
        >
        <template slot="footer">
            <a-button type="primary" key="edit">
                <router-link :to="'/package/detail/'+detail.id">
                    Modifier
                </router-link>
            </a-button>
            <a-button type="danger" key="delete" @click="deletePack(detail.id)">
                    Supprimer
            </a-button>
        </template>
            <a-card :bordered="false">
                <a-card-meta :title="detail.name"></a-card-meta>    
                <a-row type="flex" :gutter="[20,20]">
                    <a-col :span="12">
                        <a-statistic title="Prix" suffix="Fcfa" :value="detail.amount"/>
                    </a-col>
                    <a-col :span="12">
                        <a-statistic title="Durée" suffix="Jours" :value="detail.duration"/>
                    </a-col>
                    <a-col :span="24">
                        <a-statistic title="Description" :value="detail.description"/>
                    </a-col>
                </a-row>
            </a-card>
        </a-modal>
    </main>
</template>
<script>
import Axios from "axios";

const pack_columns = [
    {
        key:"name",
        title:"Nom",
        dataIndex:"name",
        scopedSlots:{customRender:"name"}
    },
    {
        key:"duration",
        title:"Duréé",
        dataIndex:"duration",
        scopedSlots:{customRender:"duration"}
    },
    {
        key:"amount",
        title:"Prix",
        dataIndex:"amount",
        scopedSlots:{customRender:"amount"}
    },
    {
        key:"action",
        title:"Action",
        scopedSlots:{customRender:"action"}
    }
]

export default {
    data(){
        return {
            packs :[],
            pack_columns,
            viewMode:false,
            detail:{}
        }
    },
    methods:{
        showDetailModal(pack){
            this.viewMode = true;
            this.detail = pack;
        },
        modalCancel(){
            this.viewMode = false;
        },
        deletePack(id){
            
            Axios.delete("http://localhost:8000/package/delete/"+id).then(res=>{
                this.packs = this.packs.filter(pack=>pack.id!=id);
            })
            this.modalCancel()
        }
    },
    beforeMount(){
        Axios.get("http://localhost:8000/package/").then(response => {
            this.packs = response.data
        })
    }
}


</script>