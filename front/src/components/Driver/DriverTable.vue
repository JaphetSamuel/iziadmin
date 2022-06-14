<template>
   
    <a-row>
        <a-col :span="24" style="background-color:white">
            <a-page-header title="Driver Stats">

            </a-page-header>
        </a-col>
        <a-col :span="24" style="margin-bottom: 10px">
            
                <a-row :gutter="12" type="flex" >
                 <a-col :span="24" :lg="12" :xl="6" class="mb-24">
				
				    <WidgetCounter
					title="Chauffeurs enregistrés"
					:value="driverData.length"
					suffix="chff"/>
			     </a-col>

                 <a-col :span="24" :lg="12" :xl="6" class="mb-24">
				    <WidgetCounter
					title="Chauffeurs Activés"
					:value="driverOnline.length"
					suffix="chff"/>
			     </a-col>
                </a-row>
            
        </a-col>
        <a-col :span="24">
            <a-card class="header-solid h-full">
            <a-card-meta>
                <template #title>
                    <a-row type="flex">
                        <a-col :span="24" :md="12">
                            <h3>Conducteurs </h3>
                        </a-col>
                        <a-col :span="24" :md="12" style="display: flex; align-items: center; justify-content: flex-end">
					        <a-radio-group v-model="driverHeadersFilter" size="small">
						        <a-radio-button value="all">Tous</a-radio-button>
						        <a-radio-button value="online">En ligne</a-radio-button>
						        <a-radio-button value="enable">Activés</a-radio-button>
					        </a-radio-group>
				        </a-col>
                    </a-row>
                </template>
            </a-card-meta>
            
            <a-space>
                <a-table :columns="columns" 
                :data-source="driverData" rowKey="phone" >

                    <span slot="action" slot-scope="action">
                        <router-link :to="'/driver/'+action.id">Details</router-link>
                    </span>
                    <span slot="is_online" slot-scope="is_online">
                        <a-badge  :text="is_online? 'en linge':'hors ligne'" :color="is_online?'green':'red'"/>
                    </span>
                    <span slot="is_enabled" slot-scope="is_enabled">
                        <a-tag class="tag-status" :class="is_enabled ? 'ant-tag-primary' : 'ant-tag-muted'">
					        {{ is_enabled ? "ACTIVE" : "DESACTIVE" }}
				        </a-tag>
                    </span>
                  
                </a-table>
            </a-space>
        </a-card>
        </a-col>
        
        <a-modal
        :visible="isItemSelected" style="width:100vh">
            <template #closeIcon>
                <a-button @click="closeDetailColumn" type="default" icon="close"/>
            </template>
            <driver-column  :record="selectedItem" :handleClose="closeDetailColumn"/>
        </a-modal>
    </a-row>
</template>

<script>
import Axios from "axios"
import DriverColumn from "./DriverColumn.vue"
import WidgetCounter from "../Widgets/WidgetCounter.vue"


const columns = [
    {
        title:"NOM",
        key:"firstname",
        dataIndex:"firstname",
        fixed:"left"
    },
    {
        title:"PRENOM",
        key:"lastname",
        dataIndex:"lastname"
    },
    {
        title:"EMAIL",
        key:"email",
        dataIndex:"email"
    },
    {
        title:"TELEPHONE",
        key:"phone",
        dataIndex:"phone"
    },
    {
        title:"EN LIGNE",
        key:"is_online",
        dataIndex:"is_online",
        scopedSlots:{customRender:"is_online"}
    },
    {
        title:"ACTVATION",
        key:"is_enabled",
        dataIndex:"is_enabled",
        scopedSlots:{customRender:"is_enabled"}
    },
    {
        title:"ACTION",
        key:"action",
        scopedSlots:{customRender:"action"},
        fixed:"right"
    }
]


export default {
    components:{
        DriverColumn,
        WidgetCounter
    },
    data (){
        var driverData = []
        var isItemSelected = false
        var tableSpan =24
        var driverHeadersFilter = 'all'
        var selectedItem = {}
        return { columns, driverData, isItemSelected, tableSpan, driverHeadersFilter, selectedItem}
    },

    beforeMount :function(){
         Axios.get("http://127.0.0.1:8000/driver/").then((reponse)=>{
        this.driverData = reponse.data;
        console.log(reponse.data);
    })
    },

    computed:{
        driverOnline: function(){
            var result = this.driverData.filter((driver)=>driver.is_enabled === true)
            return result
        }
    },
    methods:{
        showDriverDetail: function(record,e){
            this.isItemSelected = true
            this.selectedItem = record
        },
        closeDetailColumn:function(){
            this.isItemSelected = false
        },
    },

}

</script>