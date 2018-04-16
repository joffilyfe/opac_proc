# coding: utf-8
from opac_proc.core.process import ProcessExtractBase
from opac_proc.web import config
from opac_proc.logger_setup import getMongoLogger

if config.DEBUG:
    logger = getMongoLogger(__name__, "DEBUG", "extract")
else:
    logger = getMongoLogger(__name__, "INFO", "extract")


class ProcessExtractCollection(ProcessExtractBase):
    model_name = 'collection'
    task_for_selected = 'opac_proc.extractors.jobs.task_extract_selected_collections'
    task_for_all = 'opac_proc.extractors.jobs.task_extract_all_collections'


class ProcessExtractJournal(ProcessExtractBase):
    model_name = 'journal'
    task_for_selected = 'opac_proc.extractors.jobs.task_extract_selected_journals'
    task_for_all = 'opac_proc.extractors.jobs.task_extract_all_journals'


class ProcessExtractIssue(ProcessExtractBase):
    model_name = 'issue'
    task_for_selected = 'opac_proc.extractors.jobs.task_extract_selected_issues'
    task_for_all = 'opac_proc.extractors.jobs.task_extract_all_issues'


class ProcessExtractArticle(ProcessExtractBase):
    model_name = 'article'
    task_for_selected = 'opac_proc.extractors.jobs.task_extract_selected_articles'
    task_for_all = 'opac_proc.extractors.jobs.task_extract_all_articles'


class ProcessExtractPressRelease(ProcessExtractBase):
    model_name = 'press_release'
    task_for_selected = 'opac_proc.extractors.jobs.task_extract_selected_press_releases'
    task_for_all = 'opac_proc.extractors.jobs.task_extract_all_press_releases'


class ProcessExtractNews(ProcessExtractBase):
    model_name = 'news'
    task_for_selected = 'opac_proc.extractors.jobs.task_extract_selected_news'
    task_for_all = 'opac_proc.extractors.jobs.task_extract_all_news'
