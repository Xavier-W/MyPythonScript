function RemoveFileEmptyRow(ReadFilePath,WriteFilePath)
%% 2017/06/22 by DQ
% 此算法为移除文本中空行
FidRead=fopen(ReadFilePath,'rb','ieee-le','GBK');
FidWrite=fopen(WriteFilePath,'wb','ieee-le','GBK');
while ~feof(FidRead)
    FileRowStr = fgetl(FidRead);
    %     if ~isempty(FileRowStr )
    %         fprintf(FidWrite,'%s\n',FileRowStr);
    %     end
    if ~isempty(FileRowStr) && ~all(FileRowStr==' ')
        fprintf(FidWrite,'%s\n',FileRowStr);
    end
end
fclose(FidRead);
fclose(FidWrite);
end
