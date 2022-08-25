export default {

    SET_USER(context, payload){
        console.log("vuex:" + payload);
        context.commit("USER", payload);
    },

    SET_MACHINE(context, payload){
        console.log("IP_Adress_MACHINE:" + payload);
        context.commit("MACHINE", payload);
    },

    SET_QNOTMARKEDSECURITY(context, payload){
        console.log("qNotMarkedSecurity:" + payload);
        context.commit("QNOTMARKEDSECURITY", payload);
    },

    SET_QNOTMARKEDENVIROMENT(context, payload){
        console.log("qNotMarkedEnviroment:" + payload);
        context.commit("QNOTMARKEDENVIROMENT", payload);
    },

    setipmachine(context, payload){
        console.log("IP_Adress_MACHINE:" + payload);
        context.commit("IPMACHINE", payload);
    },

    setidmachine(context, payload){
        console.log("IDMACHINE:" + payload);
        context.commit("IDMACHINE", payload);
    },

    SET_MODALSECURITY(context, payload){
        console.log("MODAL_SECURITY:" + payload);
        context.commit("MODALSECURITY", payload);
    },

    SET_MODALENVORIMENT(context, payload){
        console.log("MODAL_ENVIROMENT:" + payload);
        context.commit("MODALENVIROMENT", payload);
    },
    
}