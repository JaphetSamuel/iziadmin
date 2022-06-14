<template>
    <main >
        <a-row style="background-color:white">
            <a-col :span="24">
                <a-page-header title="Promotion">

                </a-page-header>
            </a-col>
            <a-col :span="24">
                <a-table :dataSource="data" :columns="columns" rowKey="code">
                    <span slot="start_at" slot-scope="start_at">
                        {{new Date(start_at).toLocaleDateString("fr-FR")}}
                    </span>
                    <span slot="end_at" slot-scope="end_at">
                        {{new Date(end_at).toLocaleDateString("fr-FR")}}
                    </span>
                    <span slot="isActif" slot-scope="isActif">
                        {{( Date.now() >= isActif.end_at && isActif.start_at >= Date.now())? 'actif' : 'inactif'}}
                    </span>
                    <span slot="action" slot-scope="action">
                        <router-link :to="'/promotion_detail/'+action.id">Details</router-link>
                    </span>
                </a-table>
            </a-col>
        </a-row>
    </main>
</template>

<script>
import Axios  from "axios";

const columns = [
    {
        key:"code",
        title:"Code",
        dataIndex:"code",
        scopedSlots:{customRender:"code"}
    },
    {
        key:"debut",
        title:"Debut",
        dataIndex:"start_at",
        scopedSlots:{customRender:"start_at"}
    },
    {
        key:"fin",
        title:"Fin",
        dataIndex:"end_at",
        scopedSlots:{customRender:"end_at"}
    },
    {
        key:"isActif",
        title:"Actif",
        scopedSlots:{customRender:"isActif"}
    },
    {
        key:"action",
        title:"Action",
        scopedSlots:{customRender:"action"},
        fixed:"right"
    }
]

export default {
    data(){
        return {
            columns,
            data:[],
        }
    },
    beforeCreate:function(){
        Axios.get("http://127.0.0.1:8000/promos/").then((reponse)=>{
            this.data = reponse.data;
            console.log(this.data);
        })
    },
}
</script>