% List of open inputs
nrun = 1; % enter the number of runs here
jobfile = {'E:\brain\nits\Example\Conver3Dto4D_spm_job.m'};
jobs = repmat(jobfile, 1, nrun);
matlabbatch{1}.spm.util.cat.vols = {
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_011.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_012.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_013.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_014.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_015.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_016.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_017.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_018.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_019.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_020.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_021.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_022.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_023.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_024.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_025.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_026.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_027.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_028.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_029.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_030.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_031.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_032.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_033.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_034.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_035.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_036.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_037.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_038.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_039.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_040.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_041.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_042.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_043.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_044.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_045.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_046.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_047.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_048.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_049.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_050.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_051.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_052.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_053.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_054.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_055.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_056.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_057.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_058.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_059.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_060.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_061.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_062.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_063.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_064.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_065.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_066.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_067.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_068.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_069.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_070.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_071.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_072.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_073.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_074.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_075.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_076.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_077.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_078.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_079.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_080.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_081.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_082.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_083.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_084.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_085.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_086.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_087.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_088.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_089.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_090.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_091.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_092.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_093.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_094.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_095.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_096.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_097.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_098.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_099.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_100.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_101.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_102.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_103.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_104.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_105.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_106.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_107.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_108.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_109.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_110.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_111.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_112.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_113.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_114.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_115.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_116.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_117.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_118.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_119.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_120.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_121.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_122.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_123.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_124.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_125.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_126.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_127.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_128.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_129.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_130.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_131.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_132.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_133.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_134.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_135.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_136.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_137.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_138.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_139.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_140.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_141.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_142.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_143.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_144.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_145.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_146.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_147.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_148.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_149.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_150.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_151.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_152.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_153.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_154.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_155.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_156.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_157.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_158.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_159.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_160.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_161.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_162.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_163.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_164.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_165.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_166.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_167.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_168.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_169.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_170.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_171.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_172.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_173.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_174.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_175.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_176.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_177.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_178.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_179.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_180.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_181.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_182.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_183.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_184.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_185.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_186.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_187.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_188.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_189.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_190.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_191.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_192.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_193.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_194.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_195.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_196.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_197.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_198.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_199.nii,1'
                                    'J:\AD\MCAD\REST\AD_S02\AD_S02_RS\1_NC002\Rest_200.nii,1'
                                    };
%%
matlabbatch{1}.spm.util.cat.name = '4D.nii';
matlabbatch{1}.spm.util.cat.dtype = 0;
matlabbatch{1}.spm.util.cat.RT = NaN;




inputs = cell(0, nrun);
for crun = 1:nrun
end
spm('defaults', 'FMRI');
spm_jobman('run', jobs, inputs{:});