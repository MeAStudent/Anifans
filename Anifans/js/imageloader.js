var oParent = document.getElementById('container');

window.addEventListener('load',() => {
    imgLocation('box');

    function tmp_imgData(){
        this.src = [];
    }
    
    function makeimgData(n) {
      var tmp = new Array(n);
      for (var i = 0; i < n; ++i) {
        tmp[i] = new tmp_imgData();
      }
      return tmp
    }
    
    var imgData = makeimgData(40);
    
    var filenum = 1;
    
    for (var i = 0; i < imgData.length; ++i) {
        imgData[i].src = filenum + i + '.jpg'
    }
    
    console.log(imgData)

    this.addEventListener('scroll', () => {
        if(checkLoading('box')) {
            imgData.map((current) => {
                const oDiv = document.createElement('div');
                oDiv.className = 'box';
                oParent.appendChild(oDiv); 
                const boxImg = document.createElement('div');
                boxImg.className = 'box-img';
                oDiv.appendChild(boxImg);
                const img = new Image();
                img.src = 'images/'+current.src+'';
                boxImg.appendChild(img);
            });
            imgLocation('box');
        }
    });
});

const checkLoading = (child) => {
    const aContent = getChilds(child);
    const lastTop = aContent[aContent.length-1].offsetTop;
    const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    const pageHeight = document.documentElement.clientHeight || document.body.clientHeight;
    if (scrollTop + pageHeight > lastTop) {
        return true;
    }
}

const imgLocation = (child) => {
    const aContent = getChilds(child);
    const imgWidth = aContent[0].offsetWidth;
    const num = ~~(document.documentElement.clientWidth / imgWidth);
    oParent.style.cssText = 'width: '+imgWidth * num+'px; margin: 0 auto;';
    const heightArr = [];
    [].map.call(aContent, (current, index) => {
        if (index < 5) {
            heightArr.push(current.offsetHeight); 
        } else {
            const minHeight = Math.min(...heightArr);
        }
    });
}

const getChilds = (child) => {
    const childArr = [];
    const tgasAll = oParent.getElementsByTagName('*');
    [].map.call(tgasAll, (current) => {
        if (current.className == child) {
            childArr.push(current);
        } 
    });
    return childArr; 
}