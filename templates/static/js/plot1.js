let dom = document.getElementById("main");
let myChart = echarts.init(dom);
let app = {};
option = null;
option = {
    title: {
        text: '\n历年不同方式阅读率折线堆叠图'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['图书阅读率(%)','数字化阅读接触率(%)','手机阅读率(%)']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2010','2011','2012','2013','2014','2015','2016']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'图书阅读率(%)',
            type:'line',
            stack: '总量',
            data:[52.3, 53.9, 54.9, 57.8, 58.0, 58.4, 58.8]
        },
        {
            name:'数字化阅读接触率(%)',
            type:'line',
            stack: '总量',
            data:[32.8, 38.6, 40.3, 50.1, 58.1, 64.0, 68.2]
        },
        {
            name:'手机阅读率(%)',
            type:'line',
            stack: '总量',
            data:[23.0, 27.6, 32.2, 41.9, 51.9, 60.0, 66.1]
        }
    ]
};
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}